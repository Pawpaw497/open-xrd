
from uuid import uuid4

import numpy as np
from numpy.typing import ArrayLike


class Curve:

    def __init__(self, x: ArrayLike, y: ArrayLike, file_id: str, label: str):
        self.id = uuid4().hex
        self.raw_x = np.array(x)
        self.raw_y = y
        self.file_id = file_id
        self.label = label

        self.style = None

        self.displayed_x = x
        self.displayed_y = y

        self.baseline = None

    def set_style(self):
        ...
