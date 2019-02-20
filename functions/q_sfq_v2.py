import math
from functions.parent import Function
from integrator.trapezium import trapeziumrule

"""
q_sfq class: calculates integrand appearing in q(z) for the SFQ Model
(quintessence),given values for the present transition scale factor a_t, matter
density and Omega_m_0
"""

class q_sfq_integrand(Function):
    def __init__(self, a_t, omeM):
        Function.__init__(self)
        #set values of tau, a_t, omeM
        self.tau = 0.33
        self.a_t = a_t
        self.omeM = omeM

    #cal Method: Calculates integral appearing in H(a)
    #           Inputs: redshift variable x,
    #           Outputs: none
    def cal(self, x):
        w_term = 1 + self.wf + (self.wpas - self.wf)/(1 + math.pow(((self.a0/self.a_t)*(1/(1+x))), (1/self.tau)))
        #integrand appearing in function
        integrand = 3 * w_term * (1/(1+x))
        return integrand

"""
q_sfq class: calculates q(z) for the SFQ Model (quintessence),
given values for the present transition scale factor a_t, matter
density Omega_m_0 and the redshift z
"""

class q_sfq(Function):
    def __init__(self):
        Function.__init__(self)
        #ascribe integrand to function, seetting default values of a_t, omeM
        self.integrand = q_sfq_integrand(a_t = 0.5, omeM = 0.308)
        #set value of tau
        self.tau = 0.33

    #update Method: Assigns a value of Omega_m_0 and a_t to q(z)
    #           Inputs: values of Omega_m_0 and a_t
    #           Outputs: none
    def update(self, a_t, omeM):
        self.omeM = omeM
        self.a_t = a_t

    #cal Method: Calculates q(z)
    #           Inputs: redshift z
    #           Outputs: the result of the function from given values
    def cal(self, z):
        #integrate integral for given z
        q_integral = trapeziumrule(self.integrand, [0., z], 1e-5)
        #components of expression for q(z)
        w_term = self.wf + (self.wpas - self.wf)/(1 + math.pow(((self.a0/self.a_t)*(1/(1+z))), (1/self.tau)))
        q_numerator = 3 * (1-self.omeM) * (w_term) * math.exp(q_integral)
        q_denominator = (self.omeM * (1+z)**3) + ((1-self.omeM) * math.exp(q_integral))
        #function q(z)
        q = 0.5*(1 + (q_numerator / q_denominator))
        return(q)
