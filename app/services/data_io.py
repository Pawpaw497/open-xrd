# 数据管理类
from operator import ne
from pathlib import Path

import numpy as np

from app.models.curve import Curve
from app.models.file import File
from app.services.data_center import data_center


class DataIO:
    """
    Import and manage the xrd raw data.
    Can read csv, txt and xrdml format.
    """

    def __init__(self) -> None:
        self.data_center = data_center()
        pass

    def read_file(self, path: Path | str):
        '''
        Docstring for read_data

        :param self: Description
        :param path: Description
        '''
        data = np.loadtxt(path).T
        return data

    def make_curves(self, path):
        file_data = self.read_file(path)
        new_file = File(path, data=file_data)
        x_data = file_data[0, :]

        self.data_center.begin_batch()
        for i in range(file_data.shape[0]-1):
            y_data = file_data[i+1, :]
            curve = Curve(x_data, y_data, new_file.id)
            self.data_center.add_curve(curve, new_file)

        self.data_center.end_batch()

    def setup_import_configs(self, file: File):
        ...