

from pathlib import Path

import numpy as np
import requests
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QDialog, QFileDialog, QMainWindow,
                               QTableWidgetItem, QVBoxLayout)

from app.models.curve import Curve
from app.models.file import File
from app.services.data_center import data_center
from app.views.data_viewer_dock import DataViewerDock
from app.views.dialogs.baseline_dialog import BaselineDialog
from app.views.dialogs.import_config_dialog import ImportConfigDialog
from app.views.file_explorer_dock import FileExplorerDock
from app.views.plot_canvas import PlotCanvas
from app.views.ui.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    signal_plot_curve = Signal(Curve)
    signal_csv_uploaded = Signal(dict)
    signal_calculate_baseline = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenXRD")
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.data_center = data_center()

        self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.fileDock = FileExplorerDock(self)
        self.fileDock.setVisible(True)
        self.dataDock = DataViewerDock(self)
        self.dataDock.setVisible(True)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.fileDock)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dataDock)

        vLayout = QVBoxLayout()
        self._ui.centralwidget.setLayout(vLayout)

        self.canvas = PlotCanvas(self)
        vLayout.addWidget(self.canvas)

        self._set_menuBar()
        self._connect_signals()

    def _connect_signals(self):
        self._ui.actionNew_File.triggered.connect(self.import_csv)
        self.signal_csv_uploaded.connect(self.dataDock.show_table)
        self.signal_csv_uploaded.connect(self.on_file_uploaded)
        # self.signal_plot_curve.connect(self.canvas.plot_curve)

    def _set_menuBar(self):
        # File menu
        fileMenu = self.menuBar().addMenu("File")
        actionImport = QAction("Import File(s)...", self)
        actionImport.triggered.connect(self.import_csv)
        fileMenu.addAction(actionImport)

        # View menu
        self.menuBar().addMenu("View")
        viewMenu = self.menuBar().addMenu("View")

        actionViewData = QAction("Data Viewer", self)
        actionViewData.setCheckable(True)
        actionViewData.setChecked(True)
        actionViewData.toggled.connect(self.dataDock.setVisible)
        viewMenu.addAction(actionViewData)

        actionViewExplorer = QAction("File Explorer", self)
        actionViewExplorer.setCheckable(True)
        actionViewExplorer.setChecked(True)
        actionViewExplorer.toggled.connect(self.fileDock.setVisible)
        viewMenu.addAction(actionViewExplorer)

        # Tools menu
        toolsMenu = self.menuBar().addMenu("Tools")
        actionBaseline = QAction("Baseline", self)
        toolsMenu.addAction(actionBaseline)
        actionBaseline.triggered.connect(self.show_baseline_dialog)

    def import_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择 CSV 文件", "", "Text Files (*.txt; *.csv; *.dat)")
        if not file_path:
            return

        with open(file_path, 'rb') as f:
            response = requests.post(
                "http://127.0.0.1:8000/upload_csv", files={"file": f})
        if response.status_code == 200:
            data = response.json()
            self.signal_csv_uploaded.emit(data)

    def on_file_uploaded(self, data: dict):
        x = np.asarray(data["x"], dtype=float)
        y = np.asarray(data["y"], dtype=float)

        config_dialog = ImportConfigDialog(self)

        config_dialog.exec()

        curve = Curve(x, y, data["meta"]["source"], data["meta"]["source"])
        file = File(data["meta"]["source"])
        self.data_center.add_curve(curve, file)

        # self.signal_plot_curve.emit(curve)

    def show_baseline_dialog(self):
        dialog = BaselineDialog(self)
        dialog.exec()
        if dialog.accepted:
            self.signal_calculate_baseline.emit()

