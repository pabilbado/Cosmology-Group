from integrator.trapezium import trapeziumrule as integrate
from functions.parent import Function
from functions.h_modgrav import h_modgrav

import matplotlib.pyplot as plt
import math

class dLintegrand(Function):

    # Initialize the function and inherit everything from the parent function
    def __init__(self):
        Function.__init__(self)
        self.h = h_modgrav()
        self.h.update(omeM = 0.308)

    # Calculate the value as a function of x
    def cal(self, x):
        h_sec = self.h.cal(x) / 31557600 #express h in s^-1
        integrand = 1. / (x**2 * h_sec)
        return (integrand)


class dL(Function):

    # Initialize the function and inherit everything from the parent function
    def __init__(self):
        Function.__init__(self)
        self.integrand = dLintegrand()

    # Calculate the value as a function of x
    def cal(self, z):
        az = self.a0/(1+z)  #value of a corresponding to z value
        return (1+z) * self.a0 * self.c * integrate(self.integrand, [az, self.a0], 1e-3)
