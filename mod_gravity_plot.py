import matplotlib.pyplot as plt
import numpy as np
from functions.sfq import dL as dLSFQ
from functions.dL_PartIII import dL as dLDGP

dL_DGP = dLDGP()
dL_LambdaCDM = dLSFQ()
dL_LambdaCDM.update(factor=0)

#create legend
legend = ([])

fig, ax = plt.subplots(figsize=(4,3))

#set x and y axis limits
ax.set_xlim(left=0.0, right=2.0)

plt.xlabel('Redshift z')           #label x axis
plt.ylabel('Luminosity Distance $d_{L}$/Mpc') #label y axis

dL_DGP.plot(ax, [0,2], 0.05)
legend = np.append(legend, ['DGP Model'])
dL_LambdaCDM.plot(ax, [0,2], 0.05)
legend = np.append(legend, ['$\\Lambda$CDM Model'])

#create legend
plt.legend(legend)

#remove white space
fig.tight_layout()

#save figure to a file
fig.savefig('plot_dL_Pt3.pdf')
