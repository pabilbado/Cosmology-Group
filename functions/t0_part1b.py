import math
from integrator.trapezium import multi as integrate
from functions.parent import Function

"""
h_modgrav class: calculates the integrand of the expression for the age of the universe t0, for a given
matter density omeM and dark energy barotropic parameter wx
"""

class t0_part1bintegrand(Function):
    def __init__(self, omeM, wx):
        Function.__init__(self)
        self.omeM = omeM
        self.wx = wx

    #cal Method: Calculates the integrand of t_0
    #           Inputs: scale factor a
    #           Outputs: the result of the function from given values.
    def cal(self, a):
        first_term = self.omeM * math.pow(self.a0, 3) * math.pow(a, -1)

        second_term = (1-self.omeM) * math.pow(self.a0, 3*(1+self.wx))* math.pow((a), -(3*self.wx + 1))

        integrand = 1./(self.H0_1 * math.pow((first_term + second_term), 0.5))
        return integrand

"""
t0_part1b class: calculates the integral to find the age of the universe t0 in Gyr.
"""

class t0_part1b(Function):
    def __init__(self):
        Function.__init__(self)
        self.integrand = t0_part1bintegrand(omeM = 0.3, wx=-0.3)

    #cal Method: Calculates the integrand of t_0
    #           Inputs: booleans representing matter density (omeM) and barotropic parameter (wx)
    #           Outputs: updated value of the integrand. Only updates the values if omeM and/or wx are specified a (numerical) value   
    
    def update(self, omeM=False, wx=False):
        #if wx is specified, find integrand for that w_x value. Otherwise calculate using previously set value
        if type(wx) == type(False):
            wx = self.integrand.wx
        #if omeM is specified, find integrand for that w_x value. Otherwise calculate using previously set value
        if type(omeM)== type(False):
            omeM = self.integrand.omeM
        #calculate integral
        self.integrand = t0_part1bintegrand(omeM = omeM, wx=wx)

    #cal Method: Calculates the integrand of t_0
    #           Inputs: passed matter density PomeM
    #           Outputs: the result of the function from given values.
    def cal(self, PomeM):
        self.update(omeM=PomeM)
        #integrate from a lower value of 1e-5, and a step of 1e-3
        return integrate(self.integrand, [1e-5, self.a0], 1e-3) *1e-9 #express result in Gyr
