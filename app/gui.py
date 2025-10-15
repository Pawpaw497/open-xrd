# gui.py
import sys

import requests
from PySide6.QtWidgets import (QApplication, QFileDialog, QPushButton,
                               QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget)

API_URL = "http://127.0.0.1:8000"


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV Viewer")
        self.resize(800, 600)

        layout = QVBoxLayout()
        self.button = QPushButton("导入 CSV")
        self.button.clicked.connect(self.import_csv)
        self.table = QTableWidget()

        layout.addWidget(self.button)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def import_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择 CSV 文件", "", "CSV Files (*.csv)")
        if not file_path:
            return

        with open(file_path, 'rb') as f:
            response = requests.post(
                "http://127.0.0.1:8000/upload_csv", files={"file": f})
        if response.status_code == 200:
            data = response.json()
            self.show_table(data)

    def show_table(self, data):
        columns = data["columns"]
        rows = data["rows"]

        self.table.setColumnCount(len(columns))
        self.table.setRowCount(len(rows))
        self.table.setHorizontalHeaderLabels(columns)

        for i, row in enumerate(rows):
            for j, col in enumerate(columns):
                self.table.setItem(i, j, QTableWidgetItem(str(row[col])))


def run_gui():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
