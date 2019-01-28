#Matthew Gorton
#program to plot the age of the universe (consisting of matter and cosmological constant) as a function of omega_m, 
#includes lines depicting 1-sigma and 2-sigma range of Omega_m,0 and t_0


"""NEEDS COMMENTING"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #plt.xkcd()
    #Hubble Constant H_0 in units of km sec^-1 Mpc^-1
    H_0 = 73.2
    #Convert units of H_0 to yr^-1
    H_0_yrs = H_0*((31557600)*(10**3)/(3.08567758*10**22)) #s yr^-1 * km m^-1 *

    omega_m = np.arange(0.01, 1, 0.05)                                                              #range of omega_m 0<omega_m<1
    #expression for age of universe
    t_0 = (2.0/3.0)*(1/H_0_yrs)*(1/(1-omega_m)**0.5)*np.log((1+(1-omega_m)**(0.5))/(omega_m)**0.5)
    t_0_normalised = t_0/(10**9)                                                                    #express t_0 in Gyr

    #age of universe (constrained by observations of globular cluster ages)
    t_obs = 12.8                            #mean value
    t_obs_error = 1.1                       #1-sigma error
    
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
   
    #create figure to plot
    fig, ax =plt.subplots()
    plt.xlabel('${\Omega}_{m,0}$')                  #label x axis
    plt.ylabel('Age of Universe / Gyr')           #label y axis

    #plot t_0 as a function of omega_m
    ax.plot(omega_m, t_0_normalised, 'b-')
    
    #plot line showing upper and lower 1-sigma bound on t_0
    ax.plot([0.0,1.0],[t_min_1sigma, t_min_1sigma], color='#778899', linestyle='--', linewidth=1)
    ax.plot([0.0,1.0],[t_max_1sigma, t_max_1sigma], color='#778899', linestyle='--', linewidth=1)
    #plot line showing upper and lower 1-sigma bound on t_0
    ax.plot([0.0,1.0],[t_min_2sigma, t_min_2sigma], color='#B0C4DE', linestyle='--', linewidth=1)
    ax.plot([0.0,1.0],[t_max_2sigma, t_max_2sigma], color='#B0C4DE', linestyle='--', linewidth=1)
    #plot line showing upper and lower 1-sigma bound on omega_m
    ax.axvline(x=omega_min_1sigma, ymin=0.0, ymax=1.0, color='#778899', linestyle='--', linewidth=1)
    ax.axvline(x=omega_max_1sigma, ymin=0.0, ymax=1.0, color='#778899', linestyle='--', linewidth=1)
    #plot line showing upper and lower 2-sigma bound on omega_m
    ax.axvline(x=omega_min_2sigma, ymin=0.0, ymax=1.0, color='#B0C4DE', linestyle='--', linewidth=1)
    ax.axvline(x=omega_max_2sigma, ymin=0.0, ymax=1.0, color='#B0C4DE', linestyle='--', linewidth=1)

    #show figure, with all four lines
    plt.show()
