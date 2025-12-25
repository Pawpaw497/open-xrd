from PySide6.QtWidgets import QDialog, QButtonGroup
from app.views.ui.import_config_ui import Ui_importConfigDialog
from app.models.axis_types import XType, YType, DataType

wavelength_dict = {
    "Cu": 1.5418,
    "Mo": 2.7107,
    "W": 2.8188,
    "Fe": 5.6432,
    "Co": 6.2175,
    "Ni": 7.8810,
    "Cd": 9.3655,
    "Pt": 12.3984,
    "Au": 12.3984,
}


class ImportConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_importConfigDialog()
        self._ui.setupUi(self)
        self.xtypeGroup = QButtonGroup()
        self.xtypeGroup.addButton(self._ui.twoThetaButton, 0)
        self.xtypeGroup.addButton(self._ui.dSpacingButton, 1)
        self.xtypeGroup.button(0).setChecked(True)
        self.ytypeGroup = QButtonGroup()
        self.ytypeGroup.addButton(self._ui.intensityButton, 0)
        self.ytypeGroup.addButton(self._ui.normIntensityButton, 1)
        self.ytypeGroup.button(0).setChecked(True)
        self.dataTypeGroup = QButtonGroup()
        self.dataTypeGroup.addButton(self._ui.xrdButton, 0)
        self.dataTypeGroup.addButton(self._ui.xrrButton, 1)
        self.dataTypeGroup.button(0).setChecked(True)

        self.setFocus()

        for key in wavelength_dict:
            self._ui.wavelengthComboBox.addItem(
                f"{key}: {wavelength_dict[key]}", userData=wavelength_dict[key])

    def get_import_config(self):
        return ImportConfig(
            x_type=self.xtypeGroup.checkedId(),
            y_type=self.ytypeGroup.checkedId(),
            data_type=self.dataTypeGroup.checkedId(),
            wavelength=self._ui.wavelengthComboBox.currentData(),
        )


class ImportConfig:
    def __init__(self, x_type, y_type, data_type, wavelength) -> None:
        self.x_type = XType.TWO_THETA if x_type == 0 else XType.D_SPACING
        self.y_type = YType.INTENSITY if y_type == 0 else YType.NORMALIZED_INTENSITY
        self.data_type = DataType.DIFFRACTION if data_type == 0 else DataType.REFLECTION
        self.wavelength = wavelength


# # test
# if __name__ == "__main__":
#     from PySide6.QtWidgets import QApplication
#     app = QApplication()

#     dlg = ImportConfigDialog()
#     dlg.accepted.connect(lambda: print(dlg.get_import_config().__dict__))
#     dlg.show()
#     app.exec()
