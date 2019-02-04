from integrator.trapezium import multi as integrate
from functions.dCPL import dCPL, dBAO
from data.getdata import datalist

import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import math

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm



d = dCPL()
db = dBAO()

data = datalist()

rangwa=[-10,10]
rangwp=[-10,10]
step = 0.1

tolerance = 100

inpdata = []
for n, z in enumerate(data["z"]):
    inpdata.append([z, data["theta"][n]])



results = []

for datapoint in inpdata:
    z = datapoint[0]
    theta = datapoint[1]

    d0_data=db.cal(theta)
    WA = arange(rangwa[0], rangwa[1]+step, step)
    WP = arange(rangwa[0], rangwa[1]+step, step)

    for wa in WA:
        d.update(wa = wa)
        for wp in WP:
            d.update(wp=wp)
            d0_cal = d.cal(z)

            if abs(d0_cal-d0_data) <= tolerance:
                results.append({"wa":wa, "wp":wp, "do_cal": d0_cal, "d0_data": d0_data, "z": z})


filtered = []
for result in results:
    cwa = result["wa"]
    cwp = result["wp"]

    viewedz = []
    for r in results:
        if cwa == r["wa"] and cwp == r["wp"]:
            if r["z"] not in viewedz:
                viewedz.append(r["z"])

    if len(viewedz) == len(inpdata):
        filtered.append([cwa, cwp])




print(results)
print()
print(filtered)
