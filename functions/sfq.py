from integrator.simpsons import multi as integrate
from integrator.simpsons import simpsrule as integratechild
import math
from functions.parent import Function

"""
rho_integrand class: calculates the integrand for the density rho(a) for the SFQ model
"""

class rho_integrand(Function):
    def __init__(self):
        Function.__init__(self)
        self.factor = 1.
        self.wf = -1.
        self.wpast = 0.
        self.tau = 0.33
        self.at = 0.5

    #cal Method: Calculates the integrand of rho(a)
    #           Inputs: scale factor a
    #           Outputs: integrand of rho(a)
    def cal(self, a):
        #w_x term
        wx = self.wf + self.factor * (self.wpast - self.wf)/(1 + math.pow(a/self.at, 1/self.tau))
        return (1/a) * 3 * (1 + wx)


"""
rho class: calculates the density rho(a) for the SFQ model
"""
class rho(Function):
    def __init__(self):
        Function.__init__(self)
        self.integrand = rho_integrand()

    #cal Method: Calculates the density rho(a)
    #           Inputs: scale factor a
    #           Outputs: density rho(a)
    def cal(self, a):
        result = -integratechild(self.integrand, [self.a0, a], 1e-3)
        return math.exp(result)

"""
dsfq_integrand class: calculates the integrand for the physical distance in the SFQ Model
"""
class dsfq_integrand(Function):

    def __init__(self):
        Function.__init__(self)
        self.rho = rho()
        self.wpast = 0.
        self.wf = -1.

    #cal Method: Calculates the integrand of the physical distance d(a)
    #           Inputs: scale factor a
    #           Outputs: integrand for d(a)
    def cal(self, a):

        sqrt_part = math.sqrt(  self.omeM*math.pow((self.a0/a),3) + self.omeX*self.rho.cal(a)      )

        integrand = (self.c * self.a0 / math.pow(a,2)) * 1/(self.H0_2 * sqrt_part)

        return integrand

"""
dsfq_integrand class: calculates the integrand for the physical distance in the SFQ Model
"""
class dsfq(Function):
    def __init__(self):
        Function.__init__(self)
        self.integrand = dsfq_integrand()

    #cal Method: Calculates the physical distance d(a)
    #           Inputs: redshift z
    #           Outputs: physical distance d(a)
    def cal(self, z):
        #express scale factor in terms of redshift
        a = self.a0/(1+z)
        return integratechild(self.integrand, [a, self.a0], 1e-3)

    #update Method: Assigns values to calculate the physical distance d(a)
    #           Inputs: see below
    #           Outputs: none
    def update(self,
                     factor=False,  #set = 0 for Lambda_CDM, =1 for SFQ models
                     omeM=False,    #present density parameter for matter
                     omeX=False,    #present density parameter for dark energy
                     at=False,      #scale factor at transition, appearing in SFQ models
                     tau=False,     #transition width, appearing in SFQ models
                     wpast = False, #value of barotropic parameter w(a) as a -> 0
                     wf = False     #value of barotropic parameter w(a) as a -> infinity
                     ):

        if type(factor) != type(False):
            self.integrand.rho.integrand.factor = factor
        if type(omeM) != type(False):
            self.integrand.omeM = omeM
        if type(omeX) != type(False):
            self.integrand.omeX = omeX
        if type(at) != type(False):
            self.integrand.rho.integrand.at = at
        if type(tau) != type(False):
            self.integrand.rho.integrand.tau = tau
        if type(wpast) != type(False):
            self.integrand.rho.integrand.wpast = wpast
        if type(wf) != type(False):
            self.integrand.rho.integrand.wf = wf
