"""
Purpose: plot the age of the universe as a function of omega_m for a range of
         w_x values

@authors Pablo Bilbao, Matthew Gorton
@version 2.0
created 31 January 2019
updated 2 February 2019

"""

from integrator.trapezium import trapeziumrule as integrate
from functions.t0_part1b import t0_part1b as t0
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
import numpy as np

fig, ax = plt.subplots()

#create function
tfunc = t0()

#create an empty array (of strings), to display as a legend
wx_legend = ([])

#produce a plot for each w_x value
for x in np.arange(-.9,-.3, 0.2):
    tfunc.update(wx = x)
    tfunc.plot(ax, [0.1,.9], 0.1)
    #add label to legend, with the appropriate w_x value
    #use np.around to round w_x values to 1DP
    wx_legend = np.append(wx_legend, ['$w_{x}$ = ' + str(np.around(x, decimals = 1))])
    #print value of w_x and corresponding value of t0
    #tfunc.update(omeM=0.35, wx=x)
    #print(tfunc.cal(0.35))

#create plot for very large magnitude negative w
"""
for x in np.arange(-.10E9,-10E6, 10):
    tfunc.update(wx=x)
    tfunc.plot(ax, [0.1,.9], 0.1)
    #add label to legend, with the appropriate w_x value
    #use np.around to round w_x values to 1DP when displayed in legend
    wx_legend = np.append(wx_legend, ['$w_{x}$ = ' + str(np.around(x, decimals = 1))])
"""

plt.xlabel('${\Omega}_{m,0}$')                      #label x axis
plt.ylabel('Age of Universe / Gyr')                 #label y axis

#observed age of universe (from white dwarfs)
t_obs = 12.8                                        #mean value (in Gyr)
t_obs_error = 1.1                                   #1-sigma error (in Gyr)

#calculate upper and lower bounds of age to 1-sigma
t_min_1sigma = t_obs - t_obs_error
t_max_1sigma = t_obs + t_obs_error
#calculate upper and lower bounds of age to 2-sigma
t_min_2sigma = t_obs - 2*t_obs_error
t_max_2sigma = t_obs + 2*t_obs_error


#observed density parameter of matter
omega_m_obs = 0.35                                  #mean value
omega_m_error = 0.05                                #1-sigma error

#calculate upper and lower bounds of omega_m to 1-sigma
omega_min_1sigma = omega_m_obs - omega_m_error
omega_max_1sigma = omega_m_obs + omega_m_error
#calculate upper and lower bounds of omega_m to 2-sigma
omega_min_2sigma = omega_m_obs - 2*omega_m_error
omega_max_2sigma = omega_m_obs + 2*omega_m_error

#create error patches: ((x,y of bottom left corner), width, height, angle **kwargs)
t_rectangle_1sigma = Rectangle((0, t_min_1sigma), 1, 2*t_obs_error, 0, alpha = 0.5, color = 'r')
t_rectangle_2sigma = Rectangle((0, t_min_2sigma), 1, 4*t_obs_error, 0, alpha = 0.25, color = 'r')

omega_rectangle_1sigma = Rectangle((omega_min_1sigma, 7.5), 2*omega_m_error, 10, alpha = 0.5, color = 'y')
omega_rectangle_2sigma = Rectangle((omega_min_2sigma, 7.5), 4*omega_m_error, 10, alpha = 0.25, color = 'y')


# Create patch collection
pc = PatchCollection([t_rectangle_1sigma, t_rectangle_2sigma, omega_rectangle_1sigma, omega_rectangle_2sigma])
# Add collection to axes
ax.add_collection(pc)


#plot line showing upper and lower 1-sigma bound on t_0
ax.plot([0.0,1.0],[t_min_1sigma, t_min_1sigma], color='#000000', linestyle='--', linewidth=1)
ax.plot([0.0,1.0],[t_max_1sigma, t_max_1sigma], color='#000000', linestyle='--', linewidth=1)

#wx_legend = np.append(wx_legend, ['$t_{0} (1 \sigma$ error)'])

#plot line showing upper and lower 1-sigma bound on t_0
ax.plot([0.0,1.0],[t_min_2sigma, t_min_2sigma], color='#B0C4DE', linestyle='--', linewidth=1)
ax.plot([0.0,1.0],[t_max_2sigma, t_max_2sigma], color='#B0C4DE', linestyle='--', linewidth=1)

#wx_legend = np.append(wx_legend, ['$\Omega_{m,0} (1 \sigma$ error)'])

#plot line showing upper and lower 1-sigma bound on omega_m
ax.axvline(x=omega_min_1sigma, ymin=0.0, ymax=1.0, color='#778899', linestyle='--', linewidth=1)
ax.axvline(x=omega_max_1sigma, ymin=0.0, ymax=1.0, color='#778899', linestyle='--', linewidth=1)

#wx_legend = np.append(wx_legend, ['$t_{0} (2 \sigma$ error)'])

#plot line showing upper and lower 2-sigma bound on omega_m
ax.axvline(x=omega_min_2sigma, ymin=0.0, ymax=1.0, color='#B0C4DE', linestyle='--', linewidth=1)
ax.axvline(x=omega_max_2sigma, ymin=0.0, ymax=1.0, color='#B0C4DE', linestyle='--', linewidth=1)

#wx_legend = np.append(wx_legend, ['$\Omega_{m,0} (2 \sigma$ error)'])

#create legend
plt.legend(wx_legend)

#save figure to a file
fig.savefig('plot_age_universe_new.pdf')

#show figure
fig.show()

#prevents figure from immediately closing
input()
