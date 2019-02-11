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

#range of omega_m 0<omega_m<1
omega_m = np.arange(0.01, 1, 0.01)
#expression for age of universe
t_0 = (2.0/3.0)*(1/H_0_yrs)*(1/(1-omega_m)**0.5)*np.log((1+(1-omega_m)**(0.5))/(omega_m)**0.5)

#create figure
fig, ax =plt.subplots()

#add error lines for t_0
ax.plot([0.0,1.0],[t_max_1sigma, t_max_1sigma], color='r', alpha = 1, linestyle='--', linewidth=1)
ax.plot([0.0,1.0],[t_max_2sigma, t_max_2sigma], color='r', alpha = 0.5, linestyle='--', linewidth=1)
#create legend
wx_legend = np.append(wx_legend, ['$t_{0} (1 \sigma$ bound)', '$t_{0} (2 \sigma$ bound)', '$\Omega_{m,0} (1 \sigma$ bound)', '$\Omega_{m,0} (2 \sigma$ bound)'])


#set x and y axis limits
ax.set_xlim(left=0.0, right=1.0)
#ax.set_ylim(bottom=8.0, top=25.0)

#label x and y values
plt.xlabel('${\Omega}_{m,0}$')
plt.ylabel('Age of Universe / years')
#plot figure
ax.plot(omega_m, t_0, 'b-')
plt.show()
