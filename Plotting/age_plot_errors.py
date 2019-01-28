#Matthew Gorton
#program to plot the age of the universe as a function of omega_m, including upper and lower sigma values for omega


"""NEEDS COMMENTING"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #plt.xkcd()
    #Hubble Constant H_0 in units of km sec^-1 Mpc^-1
    H_0 = 73.2
    #Calculate Hubble Constant H_0 in units of yr^-1
    H_0_yrs = H_0*((31557600)*(10**3)/(3.08567758*10**22)) #s yr^-1 * km m^-1 *

    omega_m = np.arange(0.01, 1, 0.05)   #range of omega_m 0<omega_m<1
    t_0 = (2.0/3.0)*(1/H_0_yrs)*(1/(1-omega_m)**0.5)*np.log((1+(1-omega_m)**(0.5))/(omega_m)**0.5) #expression for age of universe
    t_0_normalised = t_0/(10**9) #express t_0 in Gyr

    t_mean = 12.8
    t_min_2sigma = t_mean - 2*1.1
    t_min_1sigma = t_mean - 1.1
    t_max_1sigma = t_mean + 1.1
    t_max_2sigma = t_mean + 2*1.1

    #label x and y values

    fig, ax =plt.subplots()
    plt.xlabel('${\Omega}_{m,0}$')
    plt.ylabel('Age of Universe / years')
    """
    fig1, ax1 =plt.subplots()
    plt.xlabel('${\Omega}_{m,0}$')
    plt.ylabel('Age of Universe / Gyr')
    """
    #plot function
    ax.plot(omega_m, t_0_normalised, 'b-')
    #plot upper and lower 1-sigma bound on t_0
    ax.plot([0.0,1.0],[t_min_1sigma, t_min_1sigma], color='#778899', linestyle='--', linewidth=1)
    ax.plot([0.0,1.0],[t_max_1sigma, t_max_1sigma], color='#778899', linestyle='--', linewidth=1)
    #plot upper and lower 2-sigma bound on t_0
    ax.plot([0.0,1.0],[t_min_2sigma, t_min_2sigma], color='#B0C4DE', linestyle='--', linewidth=1)
    ax.plot([0.0,1.0],[t_max_2sigma, t_max_2sigma], color='#B0C4DE', linestyle='--', linewidth=1)

    ax.axvline(x=0.30, ymin=0.0, ymax=1.0, color='#778899', linestyle='--', linewidth=1)
    ax.axvline(x=0.40, ymin=0.0, ymax=1.0, color='#778899', linestyle='--', linewidth=1)

    ax.axvline(x=0.25, ymin=0.0, ymax=1.0, color='#B0C4DE', linestyle='--', linewidth=1)
    ax.axvline(x=0.45, ymin=0.0, ymax=1.0, color='#B0C4DE', linestyle='--', linewidth=1)

    plt.show()
