from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from app.models.axis_types import XType, YType
from app.models.curve import Curve
from app.services.data_center import data_center


class PlotCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure = Figure(dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        self.ax.set_xlabel(XType.TWO_THETA)
        self.ax.set_ylabel(YType.INTENSITY)
        self.ax.grid(True, alpha=0.3)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.toolBar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolBar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.data_center = data_center()
        self.data_center.curvesChanged.connect(self.plot_curves)

    def clear(self):
        """清空画布"""
        self.ax.clear()
        self.ax.set_xlabel("2θ (deg)")
        self.ax.set_ylabel("Intensity (a.u.)")
        self.ax.grid(True, alpha=0.3)
        self.canvas.draw_idle()

    def plot_curves(self):
        """
        画多条曲线
        :param curves: 曲线列表
        """
        curves = self.data_center.curves.values()

        for curve in curves:
            self.plot_curve(curve)

        self.canvas.draw_idle()

    def plot_curve(self, curve: Curve, clear=True):
        """
        画一条曲线
        :param x: array-like
        :param y: array-like
        :param label: 曲线名
        :param clear: 是否先清空再画
        """
        if clear:
            self.clear()

        self.ax.plot(curve.displayed_x, curve.displayed_y,
                     label=curve.label, **curve.style if curve.style else {})

        if curve.baseline is not None:
            self.ax.plot(curve.displayed_x, curve.baseline,
                         label=f"{curve.label} baseline", **curve.style if curve.style else {})

        if curve.label:
            self.ax.legend()

        self.canvas.draw_idle()
