import numpy as np
from dataclasses import dataclass


@dataclass
class Capture:
    image: np.ndarray
    ret: bool
