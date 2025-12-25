from scipy.signal import find_peaks

from app.models.curve import Session


class PeakDetector:
    """
    class of peak detecting operations, 
    including peak-searching, background treatments...
    """

    def __init__(self, y, method: str, height=None,
                 threshold=None, distance=None, prominence=None,
                 width=None, wlen=None, rel_height=0.5,
                 plateau_size=None) -> None:
        super().__init__()
        self.y = y
        self.height = height
        self.threshold = threshold
        self.distance = distance
        self.prominence = prominence
        self.width = width
        self.wlen = wlen

    def detect_peaks(self, ):
        ...

    def detect_with_
