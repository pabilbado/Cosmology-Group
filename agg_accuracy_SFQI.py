import numpy as np
from functions.sfq import dsfq
import matplotlib.pyplot as plt
from functions.parent import Function

#create luminosity distance functions
dsfq1 = dsfq()
dcdm = dsfq()
#redshifts at which to calculate aggregate accuracy
z1 = 0.5
z2 = 1.32

#range of z values
rangz = np.arange(0., 2., 0.1)

#create figure and axes, set figure size
fig, ax = plt.subplots(figsize=(4,3))

#create legend
#dL_legend = ([])

#set x and y axis limits
ax.set_xlim(left=0.0, right=2.0)

plt.xlabel('Redshift z')           #label x axis
plt.ylabel('$\\Delta d_{L}/d_{L}$')              #label y axis

#create a function to calculate the aggregate accuracy
class agg_accuracy(Function):
    def __init__(self):
        Function.__init__(self)
        #physical distance for each model
        self.d = dsfq()
        self.dcdm = dsfq()
        self.dcdm.update(factor=0)

    def cal(self, z):
        #luminosity distance d_L = (1+z)d
        return np.abs((1+z) * (self.d.cal(z)-self.dcdm.cal(z))/self.d.cal(z))

#aggregate accuracy for SFQ-I model
agg1 = agg_accuracy()
agg1.d.update(factor=1, at=0.50, tau=0.33, wpast=0, wf=-1)

agg1.plot(ax, [0.01, 2.0], 0.1)
#legend = np.append(dL_legend, ['SFQ Model 1 $(a_{\\tau} = 0.50)$'])

#invert x axis
plt.gca().invert_xaxis()

#create legend
#plt.legend(legend)

#remove white space
fig.tight_layout()

#save figure to a file
fig.savefig('plot_agg_acc_PT2_SFQI.pdf')

#print aggregate accuracy at z=0.5 and z=1.32
print('SFQ-I (z = ' + str(z1) + '): ' + str(agg1.cal(z1)))
print('SFQ-I (z = ' + str(z2) + '): ' + str(agg1.cal(z2)))
