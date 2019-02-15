"""
Purpose: numerically solves for z, given a deceleration parameter q, in the DGP Model

@author Matthew Gorton
@version 1.0
14 February 2019

"""

import numpy as np
from functions.q_modgrav import q_modgrav

#create function
q = q_modgrav()

#range of z values to try
rangz = [0,5]

#set step
step = 1e-4

#tolerance - how far from the actual answer the calculated answer can be
tolerance = 0.001

#set value of omega_m,0 to best-fit Planck value
omeM = 0.308

#set value of omega_m,0 in q(z)
q.update(omeM)

#set desired value of q
q_desired = 0

#cycle through each value of z
for z in np.arange(rangz[0], rangz[1]+step, step):
    #calculate value of t_0
    val = q.cal(z)
    #print(val)

    #compare calculated value of q to actual value
    if abs(q_desired-val) <= tolerance:
        print(z)
        break
