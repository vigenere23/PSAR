import numpy as np
from abc import ABC, abstractmethod
from src.domain.vision.camera.Capture import Capture


class Camera(ABC):

    @abstractmethod
    def capture(self) -> Capture:
        pass

    @abstractmethod
    def ensure_capture(self) -> np.ndarray:
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def ensure_open(self):
        pass

    @abstractmethod
    def close(self):
        pass
