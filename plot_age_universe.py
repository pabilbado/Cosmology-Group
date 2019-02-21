"""
Purpose: plot the age of the universe as a function of omega_m for a range of
         w_x values

@authors Pablo Bilbao, Matthew Gorton
@version 4.0
created 31 January 2019
updated 11 February 2019

"""
import matplotlib.patches
from integrator.simpsons import simpsrule as integrate
from functions.t0_part1b import t0_part1b as t0
from cycler import cycler
import matplotlib as mpl
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np

#rectangle object
Rectangle = plt.Rectangle

#set colours to cycle through (shades of blue)
colours = ['#66ccff', '#3399ff', '#0066ff', '#000099']

#create figure and axes
fig, ax = plt.subplots()

#set colour cycle
ax.set_prop_cycle(color=colours)

#set x and y axis limits
ax.set_xlim(left=0.0, right=1.0)
ax.set_ylim(bottom=8.0, top=17.0)


#create function
tfunc = t0()

#create an empty array (of strings), to display as a legend
wx_legend = ([])


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


#produce a plot for each w_x value
for x in np.arange(-.9,-.3, 0.2):
    tfunc.update(wx = x)
    tfunc.plot(ax, [0.001,1.0], 0.01)
    #use np.around to round w_x values to 1DP
    wx_legend = np.append(wx_legend, ['$w_{x}$ = ' + str(np.around(x, decimals = 1))])
    #print value of w_x and corresponding value of t0

plt.xlabel('${\Omega}_{m,0}$')                      #label x axis
plt.ylabel('Age of Universe / Gyr')                 #label y axis

#create error patches: ((x,y of bottom left corner), width, height, angle **kwargs)
t_rectangle_1sigma = Rectangle((0, t_min_1sigma), 1, 2*t_obs_error, 0, alpha = 0.5, color = '#ebbaad')
t_rectangle_2sigma = Rectangle((0, t_min_2sigma), 1, 4*t_obs_error, 0, alpha = 0.25, color = '#ebbaad')

omega_rectangle_1sigma = Rectangle((omega_min_1sigma, 7.5), 2*omega_m_error, 10, alpha = 0.5, color = 'y')
omega_rectangle_2sigma = Rectangle((omega_min_2sigma, 7.5), 4*omega_m_error, 10, alpha = 0.25, color = 'y')

errorboxes = [t_rectangle_1sigma, t_rectangle_2sigma, omega_rectangle_1sigma, omega_rectangle_2sigma]
for i in range(len(errorboxes)):
    ax.add_artist(errorboxes[i])


#plot line showing lower 1-sigma bound on t_0
ax.plot([0.0,1.0],[t_min_1sigma, t_min_1sigma], color='r', alpha = 1, linestyle='--', linewidth=1)

#plot line showing lower 1-sigma bound on t_0
ax.plot([0.0,1.0],[t_min_2sigma, t_min_2sigma], color='r', alpha = 0.5, linestyle='--', linewidth=1)

#plot line showing lower 1-sigma bound on omega_m
ax.axvline(x=omega_min_1sigma, ymin=0.0, ymax=1.0, color='k', alpha = 1, linestyle='--', linewidth=1)

#plot line showing lower 2-sigma bound on omega_m
ax.axvline(x=omega_min_2sigma, ymin=0.0, ymax=1.0, color='k', alpha = 0.5, linestyle='--', linewidth=1)

#append to legend
wx_legend = np.append(wx_legend, ['$t_{0} (1 \sigma$ bound)', '$t_{0} (2 \sigma$ bound)', '$\Omega_{m,0} (1 \sigma$ bound)', '$\Omega_{m,0} (2 \sigma$ bound)'])

#plot lines showing upper 1-sigma and 2-sigma bounds of omega_m and t_0
ax.plot([0.0,1.0],[t_max_1sigma, t_max_1sigma], color='r', alpha = 1, linestyle='--', linewidth=1)
ax.plot([0.0,1.0],[t_max_2sigma, t_max_2sigma], color='r', alpha = 0.5, linestyle='--', linewidth=1)
ax.axvline(x=omega_max_1sigma, ymin=0.0, ymax=1.0, color='k', alpha = 1, linestyle='--', linewidth=1)
ax.axvline(x=omega_max_2sigma, ymin=0.0, ymax=1.0, color='k', alpha = 0.5, linestyle='--', linewidth=1)

#create legend
plt.legend(wx_legend)

#remove white space
fig.tight_layout()

#save figure to a file
fig.savefig('plot_age_universe_new.pdf')

#show figure
fig.show()

#prevents figure from immediately closing
input()
