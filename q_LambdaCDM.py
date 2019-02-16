import math
from functions.parent import Function

"""
q_LambdaCDM class: calculates q(z) for the Lamba-CDM Model,
given values for the matter density Omega_m_0 and the redshift z
"""

class q_LambdaCDM(Function):
    def __init__(self):
        Function.__init__(self)

    #update Method: Assigns a value of Omega_m_0 to q(z)
    #           Inputs: value of Omega_m_0
    #           Outputs: none
    def update(self, omeM):
        self.omeM = omeM

    #cal Method: Calculates q(z)
    #           Inputs: redshift z.
    #           Outputs: the result of the function from given values.
    def cal(self, z):
        #self.integral = trapeziumrule(self.integrand, [0., z], 1e-3)
        q_numerator = 1.5 * (self.omeM * (1+z)**3)

        q_denominator = self.omeM * (1+z)**3 + (1-self.omeM)

        q = -1 + (q_numerator / q_denominator) #function q(z)
        return(q)
