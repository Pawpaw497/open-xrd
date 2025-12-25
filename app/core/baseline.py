import numpy as np
from scipy import sparse
from scipy.interpolate import interp1d
from scipy.ndimage import minimum_filter1d
from scipy.signal import find_peaks, medfilt, savgol_filter
from scipy.sparse import csc_matrix, spdiags
from scipy.sparse.linalg import spsolve

from app.models.baseline_configs import BaselineMethod
from app.models.curve import Curve
from app.services.data_center import ParamKey, data_center


class XRDBackground:
    """
    统一的XRD背景去除工具类，支持多种背景估计算法，并可选地保护峰区域不受影响。

    支持的方法包括：SNIP、ALS、多项式拟合、滚动球、改进多项式拟合和锚点插值等。

    Unified XRD background removal with optional peak-protection
    """

    def __init__(self) -> None:
        """
        初始化XRDBackground实例。
        """
        self.data_center = data_center()

    # ------------------ 主入口 ------------------

    def compute(self, protect_peak=False,
                peak_params=None, **params):
        """
        根据指定方法计算输入数据的背景并进行扣除。

        参数:
            x : array-like
                数据横坐标（如角度或能量）。
            y : array-like
                数据纵坐标（强度或其他测量值）。
            method : str, 可选
                背景估算方法。默认为"snip"。
                可选项："snip", "als", "poly", "rolling_ball", "modpoly", "anchor"
            protect_peak : bool, 可选
                是否启用峰保护机制以避免在背景估计中误判峰为背景成分。默认False。
            peak_params : dict, 可选
                峰检测相关参数字典，仅当protect_peak=True时使用。
            **params : dict
                其他传递给具体背景算法的参数。

        返回:
            tuple:
                baseline : ndarray
                    估算出的背景曲线。
                corrected_y : ndarray
                    扣除背景后的数据。
                mask : ndarray or None
                    若启用了峰保护，则返回峰区域掩码；否则为None。
        """
        curve: Curve = next(iter(self.data_center.curves.values()))
        method = self.data_center.params.get(
            ParamKey.BASELINE_METHOD, BaselineMethod.SNIP)

        x = np.asarray(curve.displayed_x, dtype=float)
        y = np.asarray(curve.displayed_y, dtype=float)

        if protect_peak:
            mask = self._peak_mask(y, peak_params or {})
            y_for_baseline = self._apply_mask(y, mask)
        else:
            mask = None
            y_for_baseline = y

        # 调用算法
        if method == "snip":
            baseline = self.baseline_snip(y_for_baseline, **params)
        elif method == "als":
            baseline = self.baseline_als(y_for_baseline, **params)
        elif method == "poly":
            baseline = self.baseline_poly(x, y_for_baseline, **params)
        elif method == "rolling_ball":
            baseline = self.baseline_rolling_ball(y_for_baseline, **params)
        elif method == "modpoly":
            baseline = self.baseline_modpoly(x, y_for_baseline)
        elif method == "anchor":
            baseline = self.baseline_anchor(y_for_baseline, **params)
        else:
            raise ValueError("Unknown method")
        print("baseline method:", method)
        curve.baseline = baseline
        self.data_center.update_curve(curve)
        return baseline, y - baseline, mask

    # ------------------ Peak Mask ------------------
    def _peak_mask(self, y, params):
        """
        利用scipy.find_peaks自动识别峰位置，并生成一个布尔型掩码标记峰区。

        参数:
            y : array-like
                输入的一维信号数组。
            params : dict
                峰查找参数，例如：
                    height : float or None
                        最小峰高阈值。
                    prominence : float
                        峰突出度下限，默认为10。
                    distance : int
                        相邻两个峰之间的最小距离，默认为5。
                    width : int
                        每个峰左右扩展的宽度，默认为3。

        返回:
            mask : ndarray of bool
                表示峰所在区域的布尔掩码数组。
        """
        peaks, _ = find_peaks(
            y,
            height=params.get("height", None),
            prominence=params.get("prominence", 10),
            distance=params.get("distance", 5)
        )

        mask = np.zeros_like(y, dtype=bool)
        half_width = params.get("width", 3)

        for p in peaks:
            mask[max(0, p-half_width): p+half_width+1] = True

        return mask

    def _apply_mask(self, y, mask):
        """
        将峰区域的数据替换为其周围非峰区域中的最小值，从而减少其对背景估计的影响。

        参数:
            y : array-like
                原始信号数据。
            mask : array-like of bool
                峰区域的布尔掩码。

        返回:
            y2 : ndarray
                替换后的新信号数组。
        """
        y2 = y.copy()
        y2[mask] = np.min(y[~mask])
        return y2

    def baseline_snip(self, y, iterations=30):
        """
        SNIP算法实现，适用于X射线衍射图谱背景估计。

        参数:
            y : array-like
                输入信号数据。
            iterations : int, 可选
                迭代次数，默认为30次。

        返回:
            b : ndarray
                估算出的背景信号。
        """
        y = np.array(y, dtype=float)
        b = y.copy()
        L = len(y)

        for k in range(1, iterations + 1):
            # 标准 SNIP 公式：b[i] = min(b[i], (b[i-k] + b[i+k]) / 2)
            # 我们只更新中间能被索引到的部分 [k : L-k]
            left = b[0: L-2*k]      # 对应 b[i-k]
            right = b[2*k: L]       # 对应 b[i+k]
            mid = b[k: L-k]         # 对应 b[i]

            b[k: L-k] = np.minimum(mid, (left + right) / 2)
        return b

    def baseline_als(self, y, lam=1e5, p=0.01):
        """
        使用非对称最小二乘法(Asymmetric Least Squares)计算信号基线

        参数:
            y: array-like, 输入信号数据
            lam: float, 平滑参数，控制基线的平滑程度，默认为1e5
            p: float, 不对称参数，控制对峰值的惩罚程度，默认为0.01

        返回:
            z: array, 计算得到的基线信号
        """
        # 构建二阶差分矩阵用于平滑约束
        L = len(y)
        D = sparse.diags([1, -2, 1], [0, -1, -2], shape=(L, L-2))
        D = D.dot(D.T)

        # 迭代优化求解基线
        w = np.ones(L)
        for _ in range(10):
            # 构建权重矩阵和系统矩阵
            W = sparse.spdiags(w, 0, L, L)
            Z = W + lam * D
            # 求解线性方程组得到基线估计
            z = spsolve(Z, w * y)
            # 更新权重向量
            w = p * (y > z) + (1 - p) * (y <= z)

        return z

    def baseline_poly(self, x, y, degree=4):
        """
        多项式拟合作为背景估计方法。

        参数:
            x : array-like
                横坐标数据。
            y : array-like
                纵坐标数据。
            degree : int, 可选
                多项式的阶数，默认为4。

        返回:
            baseline : ndarray
                拟合出的背景曲线。
        """
        coeff = np.polyfit(x, y, degree)
        baseline = np.polyval(coeff, x)
        return baseline

    def baseline_rolling_ball(self, y, window=50):
        """
        滚动球背景估计算法，通过一维最小滤波器模拟“滚球”效果。

        参数:
            y : array-like
                输入信号数据。
            window : int, 可选
                滤波窗口大小，默认为50。

        返回:
            baseline : ndarray
                估算出的背景信号。
        """
        y = np.asarray(y)
        baseline = minimum_filter1d(y, size=window, mode='nearest')
        return baseline

    def baseline_modpoly(self, x, y, degree=5, iterations=5):
        """
        改进的多项式拟合背景估计方法，在迭代过程中排除高于当前拟合的部分。

        参数:
            x : array-like
                横坐标数据。
            y : array-like
                纵坐标数据。
            degree : int, 可选
                多项式阶数，默认为5。
            iterations : int, 可选
                迭代次数，默认为5。

        返回:
            baseline : ndarray
                估算出的背景信号。
        """
        baseline = baseline_poly(x, y, degree)
        for _ in range(iterations):
            mask = y > baseline
            coeff = np.polyfit(x[mask], y[mask], degree)
            baseline = np.polyval(coeff, x)
        return baseline

    def baseline_anchor(self, x, y, anchors):
        """
        锚点插值法构造背景曲线。

        参数:
            x : array-like
                横坐标数据。
            y : array-like
                纵坐标数据。
            anchors : list of tuples
                插值锚点列表，格式为 [(x1, y1), (x2, y2), ...]

        返回:
            baseline : ndarray
                插值得到的背景曲线。
        """
        # anchors: list of (x_pos, y_pos)
        anchors = sorted(anchors, key=lambda t: t[0])
        ax, ay = zip(*anchors)
        interp = interp1d(ax, ay, kind="linear", fill_value="extrapolate")
        baseline = interp(x)
        return baseline

    def smooth_savgol(self, y, window=11, poly=3):
        """
        Savitzky-Golay平滑滤波器，常用于降噪和平滑处理。

        参数:
            y : array-like
                待平滑的信号数据。
            window : int, 可选
                滤波窗口长度，默认为11。
            poly : int, 可选
                多项式阶数，默认为3。

        返回:
            smoothed_y : ndarray
                平滑后的信号。
        """
        return savgol_filter(y, window, poly)

    def detect_peaks_mask(self, y, height=None, distance=None,
                          half_width_factor=1.2):
        peaks, props = find_peaks(y, height=height, distance=distance)
        mask = np.ones_like(y, dtype=bool)
        # estimate FWHM-ish from prominence width if available; fallback to fixed
        widths = props.get('widths', None)
        for i, pk in enumerate(peaks):
            # half width in index units — if widths not present, use a default
            hw = (widths[i]/2) if widths is not None else 5
            ext = int(np.ceil(half_width_factor * hw))
            lo = max(0, pk - ext)
            hi = min(len(y), pk + ext + 1)
            mask[lo:hi] = False
        return mask

    def asls_baseline(self, y, lam=1e6, p=0.01, niter=10):
        L = len(y)
        D = csc_matrix(np.diff(np.eye(L), 2))
        w = np.ones(L)
        for i in np.arange(niter):
            W = spdiags(w, 0, L, L)
            Z = W + lam * D.dot(D.transpose())
            z = spsolve(Z, w*y)
            w = p * (y > z) + (1-p) * (y < z)
        return z

    def fill_mask_by_interpolation(self, x, y, mask):
        """
        插值填补被 mask 掉的峰区间
        """
        xp = x[~mask]
        yp = y[~mask]
        yi = np.interp(x, xp, yp)
        return yi

    def calculate_baseline(self, x, y):
        # Example pipeline
        x = np.arange(len(y))  # or real x-values
        mask = self.detect_peaks_mask(y)  # 你已有的 mask 布尔数组

        # 1) 插值填补（非常关键）
        y_filled = self.fill_mask_by_interp(x, y, mask)

        # 2) 可选：用 median 去除孤立噪点（不会跨越 mask 边界，因为已插值）
        y_med = medfilt(y_filled, kernel_size=5)  # kernel_size 取奇数

        # 3) 用 AsLS 拟合 baseline
        baseline = self.asls_baseline(y_med, lam=1e6, p=0.01, niter=20)

        return baseline

    def medfilt_smoothing(self, y):
        '''
        Smoothing by median filtering

        :param self: Description
        :param y: Description
        '''
        y_med = medfilt(y, kernel_size=5)
        return y_med

    def savgol_smoothing(self, x, y, windowlength, polyorder):
        '''
        Docstring for savgol_smoothing

        :param self: Description
        :param x: Description
        :param y: Description
        :param windowlength: Description
        :param polyorder: Description
        '''
        y_savgol = savgol_filter(x, y, windowlength, polyorder)
        return y_savgol

    def remove_background(self, curve: Curve):
        y = curve.displayed_y
        peaks, props = find_peaks(y)
