#Matthew Gorton
#program to plot the age of the universe as a function of omega_m

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    #Hubble Constant H_0 in units of km sec^-1 Mpc^-1
    H_0 = 73.2
    #Calculate Hubble Constant H_0 in units of yr^-1
    H_0_yrs = H_0*((31557600)*(10**3)/(3.08567758*10**22)) #s yr^-1 * km m^-1 *
    print 1/H_0_yrs

    omega_m = np.arange(0.01, 1, 0.05)   #range of omega_m 0<omega_m<1
    #t_0 = (10**11)*(1/(1-omega_m)**0.5)*np.log((1+(1-omega_m)**(0.5))/(omega_m)**0.5)
    t_0 = (2.0/3.0)*(1/H_0_yrs)*(1/(1-omega_m)**0.5)*np.log((1+(1-omega_m)**(0.5))/(omega_m)**0.5) #expression for age of universe

    #label x and y values
    plt.xlabel('${\Omega}_{m,0}$')
    plt.ylabel('Age of Universe / years')

    #plot function
    plt.plot(omega_m, t_0, 'b-')
    plt.show()
