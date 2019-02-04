"""
Purpose: numerically solves age of universe equation in the case of a flat universe
         consisting of matter and dark energy for w_x, given a value of t_0, using the Brent Algorithm

@author Matthew Gorton
@version 1.0
3 February 2019

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from integrator.trapezium import trapeziumrule as integrate
from functions.t0_part1b import t0_part1b as t0

#age of universe (constrained by observations of globular cluster ages)
t_obs = 12.8E9                            #mean value
t_obs_error = 1.1E9                       #1-sigma error

#calculate upper and lower bounds of age to 1-sigma
t_min_1sigma = t_obs - t_obs_error
t_max_1sigma = t_obs + t_obs_error
#calculate upper and lower bounds of age to 2-sigma
t_min_2sigma = t_obs - 2*t_obs_error
t_max_2sigma = t_obs + 2*t_obs_error

#observed density parameter of matter
omega_m_obs = 0.35                      #mean value
omega_m_error = 0.05                    #1-sigma error

#calculate upper and lower bounds of omega_m to 1-sigma
omega_min_1sigma = omega_m_obs - omega_m_error
omega_max_1sigma = omega_m_obs + omega_m_error
#calculate upper and lower bounds of omega_m to 2-sigma
omega_min_2sigma = omega_m_obs - 2*omega_m_error
omega_max_2sigma = omega_m_obs + 2*omega_m_error

#create age of universe function
tfunc = t0()

#dictionary of omega_m values and the corresponding bound on w_x
omegas = {omega_m_obs: 'Mean: ', omega_max_1sigma: '1-sigma upper bound: ', omega_min_1sigma: '1-sigma lower bound: ', omega_max_2sigma: '2-sigma upper bound: ', omega_min_2sigma: '2-sigma lower bound: '}
#dictionary of t_0 values and the corresponding bound on w_x
t0s = {omega_m_obs: t_obs, omega_max_1sigma: t_min_1sigma, omega_min_1sigma: t_max_1sigma, omega_max_2sigma: t_min_2sigma, omega_min_2sigma: t_max_2sigma}

#calculated age of universe - observed age of universe
def f(x, i):
    tfunc.update(omeM = i, wx=x)
    y = tfunc.cal(i) - t0s[i]
    return y

#create text file
text_file = open("Output.txt", "w")

#cycle through dictionary entries (each entry corresponds to an omega_m value)
for i in omegas:
    #solve for w_x
    x = scipy.optimize.brentq(f, -2.0, 0.0, i)
    #print result
    print(omegas[i] + str(x))
    #check age
    print(str(f(x, i) + t0s[i]))

    #write to text file
    text_file.write("%s %f" % (omegas[i], x) + "\n")

#close text file
text_file.close()
