from fuzzy_systems.core.linguistic_variables.linguistic_variable import LinguisticVariable
from fuzzy_systems.core.membership_functions.lin_piece_wise_mf import LinPWMF


class ThreePointsLV(LinguisticVariable):
    """
    Syntactic sugar for simplified linguistic variable with only 3 points (p1,
    p2 and p3) and fixed labels ("low", "medium" and "high").


      ^
      | low      medium           high
    1 |XXXXX       X          XXXXXXXXXXXX
      |     X     X  X       XX
      |      X   X    X    XX
      |       X X      XX X
      |       XX        XXX
      |      X  X     XX   XX
      |     X    X XX       XX
      |    X       X          XX
    0 +-------------------------------------->
           p1     p2          p3


    """

    def __init__(self, name, p1, p2, p3, n1="low", n2="medium", n3="high"):
        """
        :param name: name of the linguistic variable (e.g. "Temperature")
        :param p1: 1st point of the LV: "low" part of the membership function
        is 1 at this point, "medium" part of the membership function is 0 at
        this point
        :param p2: 2nd point of the LV: "low" and ""high" parts of the
        membership function are 0 at this point, "medium" part is 1
        :param p3: 3d point of the LV: "medium" part of the MF is 0 at this
        point, "high" part is 1
        :param n1: name of the fist ("low") part of the MF
        :param n2: name of the second ("medium") part of the MF
        :param n2: name of the third ("high") part of the MF
        """
        assert p1 < p2 < p3, "Points values have to be given in the increasing order"

        ling_values_dict = {
            n1: LinPWMF([p1, 1], [p2, 0]),
            n2: LinPWMF([p1, 0], [p2, 1], [p3, 0]),
            n3: LinPWMF([p2, 0], [p3, 1])
        }
        args = name, ling_values_dict
        super().__init__(*args)
