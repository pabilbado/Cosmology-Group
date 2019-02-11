from integrator.trapezium import multi as integrate
from integrator.trapezium import trapeziumrule as integratechild
import math
from functions.parent import Function

"""
sfq_integrand class: using given values for a sfq model, this class is responsible
for calculating the function inside the integral, to be used for integration in
later stages.
"""
class sfq_integrand(Function):
    def __init__(self):
        Function.__init__(self)

#cal Method: Calculates the function inside the integral.
#           Inputs:  value of a.
#           Outputs: the result of the function from given values.
    def cal(self, a):
        w = (-1 + 1./(1 + math.pow(a/self.at, 1./self.tau))) #function for the barotropic parameter in terms of a
        intgrd = -(3.*(1+w)/a)  #the full integrand
        return(intgrd)

"""
sfq_integral class: using given values for a sfq model, this class is responsible
for integrating a given function for a value of redshifts, z. (If you want a list use the wrapper in integrator.mapper.map)
"""

class sfq_integral(Function):
    def __init__(self):
        Function.__init__(self)
        self.integral = sfq_integrand()

#cal Method: Calculates the value of the scale factor from a value of z, then integrates
#the given function of the scale factor, and outputs a list of rho_x.

#            Inputs: The z value (If you want several values at once use the wrapper in the trapeziumrule)
#            Outputs: a rho_x0*(exp(3.*(1+w)/a))
    def cal(self, z):
        a = 1./(1+z)  #Calculates the values of scale factor
        integral = integratechild(self.integral, [a, self.a0], 0.001)    #integrates the integrand
        rho_x = math.exp(integral)    #Calculates rho_x for each given z, adds it to the list.
        return rho_x

class intdsfq(Function):

    def __init__(self):
        Function.__init__(self)
        self.rho = sfq_integral()
        self.z = 0

    def cal(self, a):   #calculates the integral for d(z). The integrand is long, and is therefore
                        #broken down into the constant, and the square root using variables.
        const = (self.c*self.a0)/(a**2)
        sqrt_part = self.omeM*math.pow(self.a0/a, 3) + self.omeM*self.rho.cal(self.z)
        integrand = const*(1/(self.H0_2*sqrt_part))

        return integrand

class dsfq(Function):
    def __init__(self):
        Function.__init__(self)
        self.integrand = intdsfq()

    def cal(self, a):
        return integrate(self.integrand, [a, self.a0], 0.001)

    def update(self, z = False):
        if type(z) != type(False):
            self.integrand.z = z
