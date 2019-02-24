from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from integrator.trapezium import multi as integrate
from functions.dCPL import dCPL, dBAO
from data.getdata import obtaindata
from operator import itemgetter
import pickle


d = dCPL()
db = dBAO()

inpdata = []
inpdata = obtaindata("data")

z_val = inpdata[4][0]
d0_data = inpdata[4][1]

# Define a range of graphing
rangwa=[-0.12,-0.065]
rangwp=[-1.015,-.885]
step = 0.05

WP=np.arange(rangwp[0],rangwp[1]+step,step)
WA=np.arange(rangwa[0],rangwa[1]+step,step)

with open("savedData/rdatapoint.pckl", "rb") as f:
    line = pickle.load(f)

with open("savedData/rpoint.pckl", "rb") as f:
    appr = pickle.load(f)


# Define the plot and axis
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(rangwa[0],rangwa[1])
ax.set_ylim(rangwp[0],rangwp[1])
ax.set_xlabel(r"$w_a$")
ax.set_ylabel(r"$w_p$", rotation="horizontal")
axins = ax.inset_axes([0.03, 0.5, 0.47, 0.47])

# Functions to plot.
def func(x,y):
    d.update(wa=x, wp=y)
    return d.cal(z_val)
# For the first plot calculate values
X=[]
Y=[]
Z=[]
for wa in WA:
    X.append(wa)
for wp in WP:
    Y.append(wp)

for wp in WP:
    column = []
    for wa in WA:
        column.append(func(wa,wp))
    Z.append(column)
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

# Plot it
CS = ax.contourf(X,Y,Z, 100, cmap = plt.cm.plasma, origin="lower")
axins.contourf(X,Y,Z, 100, cmap = plt.cm.plasma, origin="lower")


cbar = plt.colorbar(CS)
cbar.ax.set_ylabel(r"$d(w_a,w_p,z_0=0.5)$ in Mpc")


X=[]
Y=[]

line.sort(key=itemgetter(0))
for result in line:
    X.append(result[0])
    Y.append(result[1])
X = np.array(X)
Y = np.array(Y)

ax.plot(X,Y, "--")
axins.plot(X,Y, "--")

X=[]
Y=[]
Z=[]

for i,result in enumerate(appr):
    X.append(result[0])
    Y.append(result[1])
    Z.append(i)
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)
ax.scatter(X,Y,marker="x",c=Z,cmap= plt.cm.PiYG, vmin=-Z[-1], vmax = Z[-1])
axins.scatter(X,Y,marker="x",c=Z,cmap= plt.cm.PiYG)

axins.set_ylim(-0.98,-.97)
axins.set_xlim(-0.09675,-0.0925)
ax.indicate_inset_zoom(axins)

axins.set_xticklabels('')
axins.set_yticklabels('')


# Show the figure.
fig.tight_layout()
fig.show()
input()
