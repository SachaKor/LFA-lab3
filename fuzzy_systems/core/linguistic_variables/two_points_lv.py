from fuzzy_systems.core.linguistic_variables.linguistic_variable import \
    LinguisticVariable
from fuzzy_systems.core.membership_functions.lin_piece_wise_mf import LinPWMF


class TwoPointsPDLV(LinguisticVariable):
    """
    Syntactic sugar for simplified linguistic variable with only 2 points (p1 and
    p2) and fixed labels ("low", and "high").


      ^
      |
    1 |XXXXXXXXX                 XXXXXXXXXXX
      |        XX               XX
      |         XXX            XX
      |           XXX        XX
      |             XXX    XXX
      |               XX  XX
      |               XXXXX
      |             XXX    XXX
      |          XX           XX
      |        XX              XXX
    0 +------------------------------------>
              P<------ d ------>

    """

    def __init__(self, name, p, d, n1="low", n2="high"):
        """
        :param p: first point of the LV: "low" part of the MF is 1 at this
        point, "high" part is 0
        :param d: distance between the points where "low" and "high" parts
        parts of the MF
        :param n1: name of the first ("low") part of the MF
        :param n2: name of the second ("high") part of the MF
        """
        ling_values_dict = {
            n1: LinPWMF([p, 1], [p+d, 0]),
            n2: LinPWMF([p, 0], [p+d, 1])
        }
        args = name, ling_values_dict
        super().__init__(*args)
