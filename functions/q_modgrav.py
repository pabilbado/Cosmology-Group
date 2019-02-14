import math
from functions.parent import Function

"""
h_modgrav class: calculates q(z) for the DGP Model (a type of modified gravity),
given values for the present matter density Omega_m_0 and the redshift z
"""

class q_modgrav(Function):
    def __init__(self):
        Function.__init__(self)

    #cal Method: Calculates H(a)
    #           Inputs: value of Omega_m_0, redshift z.
    #           Outputs: the result of the function from given values.
    def cal(self, omeM, z):

        q_numerator = 6 * omeM * (1+z)**3

        q_firstterm = math.pow(((1-omeM)**2 + (4 * omeM * (1+z)**3)), 0.5)

        q_secondterm = (1-omeM) + q_firstterm

        q = -1 + (q_numerator / (q_firstterm * q_secondterm)) #function q(z)
        return(q)
