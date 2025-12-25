from PySide6.QtCore import QObject, Signal

from app.models.curve import Curve
from app.models.file import File
from app.models.project import Project


class DataCenter(QObject):
    curvesChanged = Signal()
    filesChanged = Signal()

    """
    数据中心类
    """

    def __init__(self):
        super().__init__()

        self.curves: dict[str, Curve] = {}
        self.files: dict[str, File] = {}

        self.project = Project()

        self.params = {}

        self._batch = False
        self._dirty = False

    def add_curve(self, curve: Curve, file: File):
        file.add_curve(curve)
        self.curves[curve.id] = curve

        if not self._batch:
            self.curvesChanged.emit()
        else:
            self._dirty = True

    def add_file(self, file: File):
        self.files[file.id] = file

        if not self._batch:
            self.filesChanged.emit()
        else:
            self._dirty = True

    def begin_batch(self):
        self._batch = True

    def end_batch(self):
        if self._dirty:
            self.filesChanged.emit()
            self.curvesChanged.emit()
        self._batch = False
        self._dirty = False

    def update_params(self, dict):
        self.params.update(dict)

    def update_curve(self, curve: Curve):
        self.curves[curve.id] = curve
        self.curvesChanged.emit()


_data_center = DataCenter()


def data_center() -> DataCenter:
    return _data_center


class ParamKey:
    BASELINE_METHOD = "baseline"
