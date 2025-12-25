
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QButtonGroup, QDialog

from app.core.baseline import XRDBackground
from app.models.baseline_configs import BaselineMethod
from app.services.data_center import data_center, ParamKey
from app.views.ui.baseline_ui import Ui_baselineWidget


class BaselineDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_baselineWidget()
        self._ui.setupUi(self)
        self.data_center = data_center()
        self.baseline_calculator = XRDBackground()

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self._ui.snipButton, 0)
        self.buttonGroup.addButton(self._ui.alsButton, 1)
        self.buttonGroup.addButton(self._ui.polyButton, 2)
        self.buttonGroup.addButton(self._ui.rollingButton, 3)
        self.buttonGroup.addButton(self._ui.modPolyButton, 4)
        self.buttonGroup.addButton(self._ui.anchorButton, 5)

        self._ui.buttonBox.accepted.connect(self.accept)
        self._ui.buttonBox.rejected.connect(self.reject)

    def get_baseline_method(self):
        dic = {
            0: BaselineMethod.SNIP,
            1: BaselineMethod.ALS,
            2: BaselineMethod.POLY,
            3: BaselineMethod.ROLLING_BALL,
            4: BaselineMethod.MOD_POLY,
            5: BaselineMethod.ANCHOR
        }
        return dic.get(self.buttonGroup.checkedId())

    def accept(self):
        self.data_center.update_params({
            ParamKey.BASELINE_METHOD: self.get_baseline_method()})
        super().accept()

    def reject(self):
        super().reject()
        self.close()
