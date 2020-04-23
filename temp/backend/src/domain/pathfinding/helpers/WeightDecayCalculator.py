import numpy as np


class WeightDecayCalculator:

    def __init__(self, order, max_value):
        self.__order = order
        self.__max_value = max_value

    def get_weight(self, value) -> float:
        return (1 - np.power(value / self.__max_value, 1 / self.__order)) * 100
