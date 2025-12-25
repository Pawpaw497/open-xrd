from PySide6.QtWidgets import QDockWidget, QTableWidgetItem

from app.views.ui.dataDock_ui import Ui_dataViewerDock


class DataViewerDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__()
        self._ui = Ui_dataViewerDock()

        self._ui.setupUi(self)

        self.table = self._ui.tableWidget

    def show_table(self, data: dict):
        columns = ["x", "y"]
        x = data['x']
        y = data['y']

        self.table.setColumnCount(2)
        self.table.setRowCount(len(x))
        self.table.setHorizontalHeaderLabels(columns)

        for i in range(len(x)):
            self.table.setItem(
                i, 0, QTableWidgetItem(str(x[i])))
            self.table.setItem(
                i, 1, QTableWidgetItem(str(y[i])))
