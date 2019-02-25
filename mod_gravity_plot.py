import matplotlib.pyplot as plt
from functions.dL_PartIII import dL


d_l = dL()

fig, ax = plt.subplots()

d_l.plot(ax, [0,2], 0.05)

fig.show()
input()
