"""
Purpose: numerically solves for z, given a deceleration parameter q, in the DGP Model

@author Matthew Gorton
@version 1.0
14 February 2019

"""

import numpy as np
from functions.q_LambdaCDM import q_LambdaCDM
from functions.q_sfq_v2 import q_sfq
from functions.q_modgrav import q_modgrav

#create function
q1 = q_LambdaCDM()
q2a = q_sfq()
q2b = q_sfq()
q3 = q_modgrav()

#set value of omega_m,0 to best-fit Planck value
omeM = 0.308

#set value of omega_m,0 (and a_t in SFQ models) in q(z)
q1.update(omeM)
q2a.update(omeM, 0.50)
q2b.update(omeM, 0.23)
q3.update(omeM)

#create array of q functions to cycle through
q_values = [q1, q2a, q2b, q3]

#range of z values to try
rangz = [0,5]

#set step
step = 1e-4

#tolerance - how far from the actual answer the calculated answer can be
tolerance = 0.001

#set desired value of q
q_desired = 0.

#cycle through different q functions
for q in q_values:
    #cycle through each value of z
    for z in np.arange(rangz[0], rangz[1]+step, step):
        #calculate value of q(z)
        val = q.cal(z)
        #print val

        # compare calculated value of q to actual value
        if abs(q_desired-val) <= tolerance:
            #print z if q(z) within tolerance
            print(z)
            break
