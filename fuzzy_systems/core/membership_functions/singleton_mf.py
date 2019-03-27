import numpy as np
from fuzzy_systems.core.membership_functions.lin_piece_wise_mf import FreeShapeMF

class SingletonMF(FreeShapeMF):
    def __init__(self, x):
        super().__init__(np.array([x, x]), np.array([0, 1]))

    def fuzzify(self, in_value):
        if(in_value == self._in_values[0]):
            return 1
        return 0
