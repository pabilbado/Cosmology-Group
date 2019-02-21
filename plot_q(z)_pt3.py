"""
Purpose: plots q(z) in a given redshift range, for the Lambda-CDM and DGP
models

@author Matthew Gorton
@version 1.5
16 February 2019

"""
import numpy as np
import matplotlib.pyplot as plt
from functions.q_modgrav import q_modgrav
from functions.q_sfq_v2 import q_sfq
from functions.q_LambdaCDM import q_LambdaCDM

#create functions
q1 = q_LambdaCDM()
#q2a = q_sfq()
#q2b = q_sfq()
q3 = q_modgrav()

#set value of omega_m,0 to best-fit Planck value
omeM = 0.308

#set value of omega_m,0 (and a_t in SFQ models) in q(z)
q1.update(omeM)
#q2a.update(omeM, 0.50)
#q2b.update(omeM, 0.23)
q3.update(omeM)

#range of z values
rangz = np.arange(0., 5., 0.01)

#create figure and axes
fig, ax = plt.subplots()

#set colours to cycle through (shades of blue)
colours = ['r', 'b', 'c', 'k']

#set colour cycle
ax.set_prop_cycle(color=colours)

#create legend
wx_legend = ([])

#set x and y axis limits
ax.set_xlim(left=0.0, right=5.0)

plt.xlabel('Redshift z')           #label x axis
plt.ylabel('q(z)')                 #label y axis

#plot each q value and add appropriate description to legend
q1.plot(ax, [0.0, 5.0], 0.01)
wx_legend = np.append(wx_legend, ['$\Lambda$-CDM Model'])
#q2a.plot(ax, [0.0, 5.0], 0.01)
#wx_legend = np.append(wx_legend, ['SFQ Model 1 $(a_{\\tau} = 0.50)$'])
#q2b.plot(ax, [0.0, 5.0], 0.01)
#wx_legend = np.append(wx_legend, ['SFQ Model 1 $(a_{\\tau} = 0.23)$'])
q3.plot(ax, [0.0, 5.0], 0.01)
wx_legend = np.append(wx_legend, ['DGP Model'])

#add horizontal line at q=0
ax.axhline(xmin=0.0, xmax=5.0, y=0.0, color='k', alpha = 0.5, linestyle='--', linewidth=1)

#invert x axis
plt.gca().invert_xaxis()

#create legend
plt.legend(wx_legend)

#remove white space
fig.tight_layout()

#save figure to a file
fig.savefig('plot_q(z)_pt3.pdf')

#show figure
fig.show()
