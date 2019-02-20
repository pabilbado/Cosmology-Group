from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from colorspacious import cspace_converter
from collections import OrderedDict
import numpy as np
from integrator.simpsons import multi as integrate
from functions.dCPL import dCPL, dBAO
from data.getdata import datalist


d = dCPL()
db = dBAO()
cmaps = OrderedDict()

inpdata = []
data = datalist()
for n, z in enumerate(data["z"]):
    inpdata.append([z, data["theta"][n]])

z_val = inpdata[5][0]
the_val = inpdata[5][1]
d0_data=db.cal(the_val)

# Define a range of graphing
rangwp=[-1.04,-.9]
rangwa=[-.2,0]
step = 0.008

WP=np.arange(rangwp[0],rangwp[1]+step,step)
WA=np.arange(rangwa[0],rangwa[1]+step,step)

# Define the plot and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("wa")
ax.set_ylabel("wp")
ax.set_zlabel("d")

# Functions to plot.
def func(x,y):
    d.update(wa=x, wp=y)
    return d.cal(z_val)
def plane(x,y):
    return d0_data
# For the first plot calculate values
X1=[]
Y1=[]
Z1=[]
for wa in WA:
    for wp in WP:
        X1.append(wa)
        Y1.append(wp)
        Z1.append(func(wa,wp))
X1 = np.array(X1)
Y1 = np.array(Y1)
Z1 = np.array(Z1)

surf = ax.plot_trisurf(X1, Y1, Z1, cmap=cm.summer,
                       linewidth=0, antialiased=False, alpha=0.5)
#p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.CMRmap, linewidth=0, antialiased=False)
#cb = fig.colorbar(p, shrink=0.5)

np.savetxt('points1.csv', np.c_[X1, Y1, Z1], delimiter=' ')
# Plot it
ax.plot_trisurf(X1,Y1,Z1)

# Same for the second plot
X2=[]
Y2=[]
Z2=[]
for wa in WA:
    for wp in WP:
        X2.append(wa)
        Y2.append(wp)
        Z2.append(plane(wa,wp))
X2 = np.array(X2)
Y2 = np.array(Y2)
Z2 = np.array(Z2)

np.savetxt('points2.csv', np.c_[X2, Y2, Z2], delimiter=' ')
surf = ax.plot_trisurf(X2, Y2, Z2, cmap=cm.CMRmap,
                       linewidth=0, antialiased=False, alpha=0.5)
#cb = fig.colorbar(surf, shrink=0.5)
ax.plot_trisurf(X2,Y2,Z2)



# Show the figure.
fig.show()
input()
