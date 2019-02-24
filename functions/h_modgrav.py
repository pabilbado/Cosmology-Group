import math
from functions.parent import Function

"""
h_modgrav class: calculates H(a) for the DGP Model (a type of modified gravity),
given values for the present matter density Omega_m_0 and the scale factor a
"""

class h_modgrav(Function):
    def __init__(self):
        Function.__init__(self)

    def cal(self, a):
        h0_2_yrs = self.H0_2 * (31557600) * (math.pow(10,3)) / (3.08567758 * math.pow(10,22)) #convert units of H0 from km s^-1 Mpc ^-1 to yr^-1
        h = 0.5 * self.H0_2 * ((1-self.omeM) + math.pow(((1-self.omeM)**2 + 4*self.omeM*(self.a0/a)**3), 0.5)) # function H(a)
        return(h)

    def update(self, omeM = False):
        if type(omeM)!=type(False):
            self.omeM = omeM
