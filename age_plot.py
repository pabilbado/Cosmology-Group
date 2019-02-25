"""
Purpose: plot the age of the universe as a function of omega_m for a range of
         w_x values

@authors Matthew Gorton
@version 2.0
created 26 January 2019
updated 11 February 2019

"""
import numpy as np
import matplotlib.pyplot as plt

#Hubble Constant H_0 in units of km sec^-1 Mpc^-1
H_0 = 73.2
#Calculate Hubble Constant H_0 in units of yr^-1
H_0_yrs = H_0*((31557600)*(10**3)/(3.08567758*10**22)) #s yr^-1 * km m^-1 *


#designate x axis as density parameter of the cosmological constant
omega_Lambda = np.arange(0.001, 1, 0.001)                                                        #0<omega_Lambda<1
#expression for age of universe
t_0 = (2.0/3.0)*(1/H_0_yrs)*(1/(omega_Lambda)**0.5)*np.log((1+omega_Lambda**(0.5))/(1-omega_Lambda)**0.5)

t_0_normalised = t_0/(10**9)                                                                  #express t_0 in Gyr

t_mean = 12.8
t_min_2sigma = t_mean - 2*1.1
t_min_1sigma = t_mean - 1.1
t_max_1sigma = t_mean + 1.1
t_max_2sigma = t_mean + 2*1.1


#create figure
fig, ax =plt.subplots()

#add error lines for t_0
ax.plot([0.0,1.0],[t_max_1sigma, t_max_1sigma], color='r', alpha = 1, linestyle='--', linewidth=2)
ax.plot([0.0,1.0],[t_max_2sigma, t_max_2sigma], color='r', alpha = 0.5, linestyle='--', linewidth=2)
ax.plot([0.0,1.0],[t_min_1sigma, t_min_1sigma], color='r', alpha = 1, linestyle='--', linewidth=2)
ax.plot([0.0,1.0],[t_min_2sigma, t_min_2sigma], color='r', alpha = 0.5, linestyle='--', linewidth=2)
#create legend
wx_legend = ['$t_{0} (1 \sigma$ bound)', '$t_{0} (2 \sigma$ bound)']


#set x and y axis limits
ax.set_xlim(left=0.0, right=1.0)
ax.set_ylim(bottom=8.0, top=20.0)

#add legend to plot
plt.legend(wx_legend)

#remove white space
fig.tight_layout()

#label x and y values
plt.xlabel('${\Omega}_{\Lambda,0}$')
plt.ylabel('Age of Universe / Gyr')
#plot figure
ax.plot(omega_Lambda, t_0_normalised, 'b-')
plt.show()

#save figure to a file
fig.savefig('plot_age_wx=-1.pdf')
