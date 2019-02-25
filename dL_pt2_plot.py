import matplotlib.pyplot as plt
import numpy as np
from functions.sfq import dL as dLSFQ
from functions.dL_PartIII import dL as dLDGP

dL_LambdaCDM = dLSFQ()
dL_purematter = dLSFQ()
dL_LambdaCDM.update(factor=0.)
dL_purematter.update(factor=0., omeM=1.)

dL_sfq1 = dLSFQ()
dL_sfq1.update(factor=1, at=0.50, tau=0.33, wpast=0, wf=-1)
dL_sfq2 = dLSFQ()
dL_sfq2.update(factor=1, at=0.23, tau=0.33, wpast=0, wf=-1)

#create legend
legend = ([])

fig, ax = plt.subplots(figsize=(5,4))

#set colours to cycle through
colours = ['r', 'orange', 'b', 'k']

#set colour cycle
ax.set_prop_cycle(color=colours)

#set x and y axis limits
ax.set_xlim(left=0.0, right=2.0)

plt.xlabel('Redshift z')           #label x axis
plt.ylabel('Luminosity Distance $d_{L}$/Mpc') #label y axis

dL_sfq1.plot(ax, [0,2], 0.05)
legend = np.append(legend, ['SFQ Model 1 $(a_{\\tau} = 0.50)$'])
dL_sfq2.plot(ax, [0,2], 0.05)
legend = np.append(legend, ['SFQ Model 2 $(a_{\\tau} = 0.23)$'])
dL_LambdaCDM.plot(ax, [0,2], 0.05)
legend = np.append(legend, ['$\\Lambda$CDM Model'])
dL_purematter.plot(ax, [0,2], 0.05)
legend = np.append(legend, ['Pure Matter Model'])

#create legend
plt.legend(legend)

#remove white space
fig.tight_layout()

#save figure to a file
fig.savefig('plot_dL_Pt2.pdf')
