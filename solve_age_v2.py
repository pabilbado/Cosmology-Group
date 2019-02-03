"""
Purpose: numerically solves Equation (1) - the expression for the age of the
         universe t_0 in the case of a flat universe consisting of matter and a cosmological
         constant for omega_lambda, given a value of t_0, using the Brent Algorithm

@author Matthew Gorton
@version 2.0
2 February 2019

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

if __name__ == "__main__":

    #Hubble Constant H_0 in units of km sec^-1 Mpc^-1
    H_0 = 73.2
    #Convert units of H_0 to yr^-1
    H_0_yrs = H_0*((31557600)*(10**3)/(3.08567758*10**22))

    #age of universe (constrained by observations of globular cluster ages)
    t_obs = 12.8E9                            #mean value
    t_obs_error = 1.1E9                       #1-sigma error

    #calculate upper and lower bounds of age to 1-sigma
    t_min_1sigma = t_obs - t_obs_error
    t_max_1sigma = t_obs + t_obs_error
    #calculate upper and lower bounds of age to 2-sigma
    t_min_2sigma = t_obs - 2*t_obs_error
    t_max_2sigma = t_obs + 2*t_obs_error

    sqrt = np.sqrt
    abs = np.abs

    def f(x):
        y = (2.0/3.0) * (1/H_0_yrs) * (1/sqrt(x)) * np.log((1+sqrt(x))/(sqrt(abs(1.0 - x)))) - t_max_2sigma
        return y

    x = scipy.optimize.brentq(f, 0.1, 0.9)

    print(x)
