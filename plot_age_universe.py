from integrator.trapezium import trapeziumrule as integrate
from functions import dCPL
from functions.t0_part1b import t0_part1b as t0
import matplotlib.pyplot as plt

from numpy import arange


fig, ax = plt.subplots()

tfunc = t0()

for x in arange(-.9,-.3, 0.2):
    tfunc.update(wx=x)
    tfunc.plot(ax, [0.01,.999], 0.01)
    """ADD A LEGEND!"""

tfunc.update(wx=-.9)
tfunc.plot(ax, [0.1,.9], 0.1)

#to add 1-sigma and 2-sigma lines, add ax.hline(...)

t_obs = 12.8E9                            #mean value
t_obs_error = 1.1E9                      #1-sigma error

#calculate upper and lower bounds of age to 1-sigma
t_min_1sigma = t_obs - t_obs_error
t_max_1sigma = t_obs + t_obs_error
#calculate upper and lower bounds of age to 2-sigma
t_min_2sigma = t_obs - 2*t_obs_error
t_max_2sigma = t_obs + 2*t_obs_error


#plot line showing upper and lower 1-sigma bound on t_0
ax.plot([0.0,1.0],[t_min_1sigma, t_min_1sigma], color='#778899', linestyle='--', linewidth=1)
ax.plot([0.0,1.0],[t_max_1sigma, t_max_1sigma], color='#778899', linestyle='--', linewidth=1)
#plot line showing upper and lower 1-sigma bound on t_0
ax.plot([0.0,1.0],[t_min_2sigma, t_min_2sigma], color='#B0C4DE', linestyle='--', linewidth=1)
ax.plot([0.0,1.0],[t_max_2sigma, t_max_2sigma], color='#B0C4DE', linestyle='--', linewidth=1)

"""ADD AXIS LABELS"""

fig.show()
input()
