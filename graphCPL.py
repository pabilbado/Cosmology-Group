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

z_val = inpdata[5][0]
the_val = inpdata[5][1]
d0_data=db.cal(the_val)

rangwp=[-5,10]
rangwa=[-5,10]
step = 3

WP=np.arange(rangwp[0],rangwp[1]+step,step)
WA=np.arange(rangwa[0],rangwa[1]+step,step)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("wa")
ax.set_ylabel("wp")
ax.set_zlabel("d")

def func(x,y):
    d.update(wa=x, wp=y)
    return d.cal(z_val)
def plane(x,y):
    return d0_data

X=[]
Y=[]
Z=[]
for wa in WA:
    for wp in WP:
        X.append(wa)
        Y.append(wp)
        Z.append(func(wa,wp))
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

ax.plot_trisurf(X,Y,Z)


X=[]
Y=[]
Z=[]
for wa in WA:
    for wp in WP:
        X.append(wa)
        Y.append(wp)
        Z.append(plane(wa,wp))
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

ax.plot_trisurf(X,Y,Z)



fig.show()
input()
