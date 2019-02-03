#from integrator.trapezium import multi as integrate
import math
from integrator.trapezium import trapeziumrule as integrate
from functions.parent import Function



class t0_part1bintegrand(Function):
    def __init__(self, omeM, wx):
        Function.__init__(self)
        self.omeM = omeM
        self.wx = wx

    def cal(self, x):
        first_term = self.omeM * math.pow(self.a0, 3) * math.pow(x, -1)

        second_term = (1-self.omeM) * math.pow(self.a0, 3*(1+self.wx))* math.pow((x), -(3*self.wx + 1))

        integrand = 1./(self.H0 * math.pow((first_term + second_term), 0.5))
        return integrand


class t0_part1b(Function):
    def __init__(self):
        Function.__init__(self)
        self.integrand = t0_part1bintegrand(omeM = 0.3, wx=-0.3)

        #updates the values of the integrand. Only updates the values especified a (numerical) value
    def update(self, omeM=False, wx=False):
        if type(wx) == type(False):
            wx = self.integrand.wx
        if type(omeM)== type(False):
            omeM = self.integrand.omeM
        self.integrand = t0_part1bintegrand(omeM = omeM, wx=wx)

    def cal(self, PomeM):
        self.update(omeM=PomeM)
        return integrate(self.integrand, [0.1, self.a0], 0.001)
