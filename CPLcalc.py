from integrator.trapezium import multi as integrate
from functions.dCPL import dCPL, dBAO
from data.getdata import datalist

import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import math


d = dCPL()
db = dBAO()

data = datalist()

rangwa=[-10,10]
rangwp=[-10,10]
step = 1

tolerance = 100

inpdata = []
for n, z in enumerate(data["z"]):
    inpdata.append([z, data["theta"][n]])



results = []

for datapoint in inpdata:
    z = datapoint[0]
    theta = datapoint[1]

    d0_data=db.cal(theta)


    for wa in arange(rangwa[0], rangwa[1]+step, step):
        d.update(wa = wa)
        for wp in arange(rangwp[0], rangwp[1]+step, step):
            d.update(wp=wp)
            d0_cal = d.cal(z)

            if abs(d0_cal-d0_data) <= tolerance:
                results.append([wa, wp, d0_cal, d0_data])

print(results)
