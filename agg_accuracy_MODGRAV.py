import numpy as np
from functions.sfq import dL as dsfq
import matplotlib.pyplot as plt
from functions.parent import Function
from functions.dL_PartIII import dL as dDGP

#create luminosity distance functions
d_DGP = dDGP()
d_CDM = dsfq()
#redshifts at which to calculate aggregate accuracy
z1 = 0.5
z2 = 1.32

#range of z values
rangz = np.arange(0., 2., 0.1)

#create figure and axes, set figure size
fig, ax = plt.subplots(figsize=(4,3))

#create legend
#legend = ([])

#set x and y axis limits
ax.set_xlim(left=0.0, right=2.0)

plt.xlabel('Redshift z')                         #label x axis
plt.ylabel('$\\Delta d_{L}/d_{L}$')              #label y axis

#create a function to calculate the aggregate accuracy
class agg_accuracy(Function):
    def __init__(self):
        Function.__init__(self)
        #physical distance for each model
        self.d = dDGP()
        self.dcdm = dsfq()
        self.dcdm.update(factor=0)

    def cal(self, z):
        #luminosity distance d_L = (1+z)d
        return np.abs((self.d.cal(z)-self.dcdm.cal(z))/self.d.cal(z))

#aggregate accuracy for DGP model
agg1 = agg_accuracy()

agg1.plot(ax, [0.01, 2.0], 0.1)
#legend = np.append(dL_legend, ['SFQ Model 1 $(a_{\\tau} = 0.50)$'])

#invert x axis
ax.invert_xaxis()

#remove white space
fig.tight_layout()

#save figure to a file
fig.savefig('plot_agg_acc_PT3.pdf')

#print aggregate accuracy at z=0.5 and z=1.32
print('DGP (z = ' + str(z1) + '): ' + str(agg1.cal(z1)))
print('DGP (z = ' + str(z2) + '): ' + str(agg1.cal(z2)))
