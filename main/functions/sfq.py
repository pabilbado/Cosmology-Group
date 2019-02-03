from integrator.trapezium import multi as integrate
from data.getdata import data_as_list
import math

"""
sfq_integrand class: using given values for a sfq model, this class is responsible
for calculating the function inside the integral, to be used for integration in
later stages.
"""
class sfq_integrand():
    def __init__(self):

        self.a0 = 1 #Value of a @ t0.
        self.at = 1 #This is the Scaling Factor @ Transition. PLEASE CHANGE TO GIVEN VALUE
        self.tau = 0.33 #Value of transition width.

#cal Method: Calculates the function inside the integral.
#           Inputs:  no input.
#           Outputs: the result of the function from given values.
    def cal(self, a):
        w = (-1 + 1./(1 + math.pow(a/self.at, 1./self.tau))) #function for the barotropic parameter in terms of a
        intgrd = -(3.*(1+w)/a)  #the full integrand
        return(intgrd)

"""
sfq_integral class: using given values for a sfq model, this class is responsible
for integrating a given function for a list values of redshifts, z.
"""
class sfq_integral():
    def __init__(self):

        initdata = data_as_list() #initiates class data_as_list().
        self.a0 = 1
        self.at = 1 #This is the Scaling Factor @ Transition. PLEASE CHANGE TO GIVEN VALUE
        self.tau = 0.33 #Value of transition width.
        self.rho_x0 = 1 #set to 1 for now - PLEASE CHANGE TO CALCULATED VALUE
        self.z =  initdata.datalist()  #Given values of redshifts

#cal Method: Calculates the value of the scale factor from a list of z, then integrates
#the given function of the scale factor, and outputs a list of rho_x.

#            Inputs: no input.
#            Outputs: a list of rho_x resulted from the rho_x0*(exp(3.*(1+w)/a))
    def cal(self):
        rho_x = []  #Stores the values of rho_x here.
        for num in self.z:
            a = 1./(1+num)  #Calculates the values of scale factor

            integral = integrate(sfq_integrand(), [a, self.a0], 0.001)    #integrates the integrand
            rho_x.append(math.exp(integral))    #Calculates rho_x for each given z, adds it to the list.
        return rho_x
