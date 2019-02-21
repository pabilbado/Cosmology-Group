import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from functions.sfq import dsfq
from data.getdata import obtaindata
import math

cosmo_const = dsfq()

# results = obtaindata('data.csv')
# for datapoint in results:
#     z = datapoint[0]
#     d_z = datapoint[1]
cosmo_const.update(factor = 0)
fig, ax = plt.subplots()
cosmo_const.plot(ax, [0.2,1.7], 0.1)

cosmo_const.update(factor=1, at=0.50, tau=0.33, wp=0, wm=0, wf=-1)
cosmo_const.plot(ax, [0,1.7], 0.1)
cosmo_const.update(factor = 1, at=0.23, tau=0.33, wp=0, wm=0, wf=-1)
cosmo_const.plot(ax, [0, 1.7], 0.1)
ax.set_xlabel(r'$z$')
ax.set_ylabel(r'$d_L$') #to Alice: find out the units

fig.show()
input()
