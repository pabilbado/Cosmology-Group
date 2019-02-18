from integrator.trapezium import multi as integrate

import matplotlib.pyplot as plt
import numpy as np
import math


"""
The parent function with the default methods of plotting and calculation for f(x)=x,
Using inheritance we can create new functions that will by default look like this incluiding the variables.
And new functions will also inherit the plotting capabilities.
"""

class Function(object):
    def __init__(self):
        # List of constants

        ## General variables
        self.a0= 1.
        self.H0_1= 7.48626305E-11 # in year^-1
        self.omeM = 0.308
        self.omeX= 0.692
        self.wp= 1
        self.wa= 1
        self.wx = -1
        self.wm = 0

        ## BAO calculation in the CPL
        self.c = 2.998e5 # in km/s
        self.H0_2 = 67.81 # in Km/(s MpC)
        self.lbao = 147.6 # in MpC

        ## SFQ parametrisation variables needed
        self.tau = 0.33 #Value of transition width. SFQ
        self.at = 1 #This is the Scaling Factor @ Transition. PLEASE CHANGE TO GIVEN VALUE
        self.rho_x0 = 1 #set to 1 for now - PLEASE CHANGE TO CALCULATED VALUE
        self.wpas = 0
        self.wf = -1

    # Basic function f(x)=x
    def cal(x):
        return x

    # Plotting in axis ax
    def plot(self, ax, rang, stp):
        X = np.arange(rang[0], rang[1]+stp, stp)
        y = []
        for x in X:
            y.append(self.cal(x))
        Y = np.array(y)

        ax.plot(X,Y)
        return ax
