from app.core.baseline import XRDBackground
from app.core.pre_processing import PreProcessor
from app.services.data_center import data_center
from app.views.mainwindow import MainWindow


class WindowController:
    def __init__(self, main_window: MainWindow):
        self.main_window = main_window
        self.data_center = data_center()
        self.pre_processor = PreProcessor()

        self.baseline_calculator = XRDBackground()
        
        self._connect_signals()

    def _connect_signals(self):
        self.main_window.signal_calculate_baseline.connect(
            self.baseline_calculator.compute)

    def show_window(self):
        self.main_window.show()
