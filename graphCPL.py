from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from integrator.trapezium import multi as integrate
from functions.dCPL import dCPL, dBAO
from data.getdata import datalist


d = dCPL()
db = dBAO()

inpdata = []
data = datalist()
for n, z in enumerate(data["z"]):
    inpdata.append([z, data["theta"][n]])

z_val = inpdata[1][0]
the_val = inpdata[1][1]
d0_data=db.cal(the_val)

rang=[5,20]
step = 0.5

wa=wp=np.arange(rang[0],rang[1]+step,step)
WA, WP = np.meshgrid(wa, wp)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def func(x,y):
    d.update(wa=x, wp=y)
    return d.cal(z_val)
def plane(x,y):
    return d0_data

zs = np.array([func(x,y) for x,y in zip(np.ravel(WA), np.ravel(WP))])
Z = zs.reshape(WA.shape)
ax.plot_surface(WA, WP, Z)


zs = np.array([plane(x,y) for x,y in zip(np.ravel(WA), np.ravel(WP))])
Z = zs.reshape(WA.shape)
ax.plot_surface(WA, WP, Z)



fig.show()
input()
