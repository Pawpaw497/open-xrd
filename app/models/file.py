from app.models.curve import Curve
from pathlib import Path

from uuid import uuid4


class File:
    def __init__(self, path: str, data=[]) -> None:
        self.id = uuid4().hex
        self.filepath = Path(path)
        self.raw_data = data

        self.filename: str = Path(path).stem

        self.raw_x_type = ""
        self.raw_y_type = ""
        self.data_type = ""

        self.curves: dict[str, Curve] = {}

    def add_curve(self, new_curve):
        self.curves[new_curve.id] = new_curve

