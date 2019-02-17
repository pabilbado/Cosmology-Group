"""
Purpose: plots q(z) in a given redshift range, in the DGP Model

@author Matthew Gorton
@version 1.0
15 February 2019

"""
import numpy as np
import matplotlib.pyplot as plt
from functions.q_modgrav import q_modgrav

#create function
q = q_modgrav()

#set value of omega_m,0 to best-fit Planck value
omeM = 0.308

#set value of omega_m,0 in q(z)
q.update(omeM)

#range of z values
rangz = np.arange(0., 5., 0.01)

#create figure and axes
fig, ax = plt.subplots()

#set x and y axis limits
ax.set_xlim(left=0.0, right=5.0)

plt.xlabel('Redshift z')           #label x axis
plt.ylabel('q(z)')                 #label y axis

q.plot(ax, [0.0, 5.0], 0.01)

#save figure to a file
fig.savefig('plot_q(z)_DGP.pdf')

#show figure
fig.show()
