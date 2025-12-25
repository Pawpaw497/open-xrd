# gui.py
import sys

from PySide6.QtWidgets import QApplication

from app.views.mainwindow import MainWindow
from app.core.window_controller import WindowController

API_URL = "http://127.0.0.1:8000"


def run_gui():
    app = QApplication(sys.argv)
    win = MainWindow()
    main_controller = WindowController(main_window=win)
    main_controller.show_window()
    sys.exit(app.exec())
