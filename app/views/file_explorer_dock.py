from PySide6.QtWidgets import QDockWidget

from app.views.ui.explorerDock_ui import Ui_explorerDock
from app.views.plot_canvas import PlotCanvas


class FileExplorerDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_explorerDock()
        self._ui.setupUi(self)

