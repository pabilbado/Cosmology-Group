from integrator.trapezium import multi as integrate
from functions.dCPL import dCPL, dBAO
from data.getdata import datalist

import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import math


d = dCPL()
db = dBAO()

rangwa=[0,20]
rangwp=[0,20]
step = 0.2
tolerance = 500

data = datalist()
inpdata = []
for n, z in enumerate(data["z"]):
    inpdata.append([z, data["theta"][n]])



results = []
for n, datapoint in enumerate(inpdata):
    z = datapoint[0]
    theta = datapoint[1]

    d0_data=db.cal(theta)
    WA = arange(rangwa[0], rangwa[1]+step, step)
    WP = arange(rangwa[0], rangwa[1]+step, step)

    for i, wa in enumerate(WA):
        print( (i+(n*len(WA)))*100 / (len(WA)*len(inpdata)))
        d.update(wa = wa)
        for wp in WP:
            d.update(wp=wp)
            d0_cal = d.cal(z)

            if abs(d0_cal-d0_data) <= tolerance:
                results.append({"wa":wa, "wp":wp, "do_cal": d0_cal, "d0_data": d0_data, "z": z})


filtered = []
examined = []
for result in results:
    cwa = result["wa"]
    cwp = result["wp"]
    if [cwa, cwp] not in examined:
        examined.append([cwa, cwp])
        viewedz = []
        for r in results:
            if cwa == r["wa"] and cwp == r["wp"]:
                if r["z"] not in viewedz:
                    viewedz.append(r["z"])

        if len(viewedz) == len(inpdata):
            filtered.append([cwa, cwp])
        elif len(viewedz) >1:
            print("{Z: {0} ({1}) for wa:{2}, wp:{3}}".format(viewedz, len(viewedz),cwa, cwp))

print(filtered)
