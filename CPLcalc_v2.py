from integrator.trapezium import multi as integrate
from functions.dCPL import dCPL
from data.getdata import obtaindata
from integrator.vectors import *

import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import math
import random

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pickle
import os


"""
Find the closest solution to a set of points given the data and the function to calculate.
Taking a wa and wp, a tolerance level an initial stepsize and the function
it will output a set of points and a stepsize with a size relative to the tolerance
"""

def LineMethod(wa, wp, tolerance, step, inpdata, df):
    print("Finding point in Line")
    z = inpdata[0][0]
    d_data = inpdata[0][1]
    df = dCPL()

    pDifsign = 0
    while True:
        df.update(wa=wa, wp=wp)
        d_cal = df.cal(z)
        Dif = (d_cal - d_data)

        if abs(Dif) <= tolerance:
            print("point found on the line: [{0}, {1}]; Dif: {2}".format(wa, wp, Dif))
            break

        neigP = neighCor(wa, wp, np.array([step,0]), 10)
        d_neig = []
        for point in neigP:
            wax = point[0]
            wpx = point[1]

            d.update(wa=wax, wp=wpx)
            d_neig.append(d.cal(z)-d_cal)

        lowd = min(d_neig)
        lowp = neigP[d_neig.index(lowd)]
        higd = max(d_neig)
        higp = neigP[d_neig.index(higd)]

        if d_cal > d_data:
            wa = lowp[0]
            wp = lowp[1]
        else:
            wa = higp[0]
            wp = higp[1]

        Difsign = abs(Dif)/Dif
        if Difsign != pDifsign:
            step *=0.2

        pDifsign = Difsign
        print("{0} , {1}, Dif: {4}; step: {3}".format(wa, wp, tolerance, abs(step), Dif))
    return wa, wp, step

"""
Given a point that is a solution to the dataset and the function given, alongside with a stepsize, tolerance.
It will scan through the ranges given moving along the line perpendicular to the slope

"""


def moveLine(wa, wp, step, tolerance, inpdata ,df ,results = [], reverse = False, rangwa = [-5,5], rangwp=[-5,5]):
    z = inpdata[0][0]
    d_data = inpdata[0][1]
    Atolerance = tolerance*2
    prevV=np.array([step, 0])

    while True:
        neigP = neighCor(wa, wp, prevV, int(30), reverse = reverse)
        Small = False

        diffL = []
        for point in neigP:
            wax = point[0]
            wpx = point[1]

            df.update(wa=wax, wp=wpx)
            d_cal = df.cal(z)
            if abs(d_cal-d_data) <= tolerance and [wax, wpx] not in results:
                if not reverse:
                    if results[-1][0] < wax:
                        Small = True
                        break
                else:
                    if results[-1][0] > wax:
                        Small = True
                        break

            diffL.append(d_cal -d_data)

        if not Small:
            mdiff = min(diffL)
            mpoint = neigP[diffL.index(min(diffL))]
            Mdiff = max(diffL)
            Mpoint = neigP[diffL.index(max(diffL))]

            Mx = Mpoint[0]
            My = Mpoint[1]
            mx = mpoint[0]
            my = mpoint[1]

            if not reverse:
                wpx = ((Mx-mx)*.5) + wp
                wax = -((My-my)*.5) + wa
            else:
                wpx = -((Mx-mx)*.5) + wp
                wax = ((My-my)*.5) + wa

        d.update(wa=wax, wp = wpx)
        diff = d.cal(z)-d_data

        prevV=np.array([wax-wa,wpx-wp])
        wa = wax
        wp = wpx

        if abs(diff) >= Atolerance:
            print("Out of the line")
            wa, wp, _= LineMethod(wax, wpx, tolerance, step*.1, inpdata, df)

        if [wa,wp] not in results:
            if not reverse:
                if results[-1][0] < wa:
                    results.append([wa,wp])
                    print("[{2}] point {0}; diff {1}".format([wa,wp], diff, Small))
            else:
                if results[-1][0] > wa:
                    results.append([wa,wp])
                    print("[{2}] point {0}; diff {1}".format([wa,wp], diff, Small))

        if wa < rangwa[0] or wa > rangwa[1]:
            break
        if wp < rangwp[0] or wp > rangwp[1]:
            break
    return results

"""
Checks the set of solutions given against the dataset given
and outputs the best solution values
"""


def checkresults(results, data, tol, df):

    print(len(results))
    for datapoint in data[::-1]:
        filtered = []
        z = datapoint[0]
        d_data = datapoint[1]
        n_results=[]
        print("Calculating values")
        for value in results:
            df.update(wa=value[0], wp=value[1])
            d_cal = df.cal(z)
            diff = abs(d_cal - d_data)
            n_results.append([value, diff])
        print("Filtering results")
        prev = False
        filtered = []
        while filtered ==[]:
            for data in n_results:
                diff = data[1]
                values = data[0]
                if diff <= tol:
                    filtered.append(values)
            if filtered==[]:
                tol*=1.01
                print("No results found, increasing tolerance to {0}".format(tol))

        results = filtered
        print(len(results))
    return results

"""
Given a set of two value list, it will output the same list rounded to n (default is 2) decimal places.
Without any duplication in the list.
"""


def roundR(results, n=2):
    newresults = []
    for point in results:
        wax = round(point[0], n)
        wpx = round(point[1], n)
        if [wax, wpx] not in newresults:
            newresults.append([wax, wpx])
    return newresults

"""
Performs a linear regression test against the lBAO value and outputs the point with the best result.
"""


def linearregression(df, results, inpdata):
    from functions.dCPL import dBAO
    db = dBAO()

    rs = []
    for r in results:
        wa = r[0]
        wp = r[1]
        df.update(wa = wa, wp = wp)
        X = []
        Y =[]
        for data in inpdata:
            z = data[0]
            d = data[1]
            X.append(1./df.cal(z))
            Y.append(db.cal(d))
        X = np.array(X)
        Y = np.array(Y)
        mean = 0
        for y in Y:
            mean+=y
        mean = mean/len(Y)



        a=0
        b=0
        for y, x in zip(Y, X):
            a+=math.pow((y-(db.lbao*x)),2)
            b+=math.pow(y-mean, 2)
        rs.append([r,1-(a/b)])

    for r in rs:
        if r[1] > 1 or r[1] < 0:
            rs.remove(r)

    rsmin = max([item[1] for item in rs])
    for r in rs:
        if rsmin == r[1]:
            print(r)



d = dCPL()

step = 5*10          # Initial stepsize
tolerance = 1     # Tolerace
iP = [-9, 20]        # Initial point
ranges = [[-15,10],  # Wa range &
          [0,30]]  # Wp range to examine


inpdata = obtaindata("data_test")

wa = iP[0]
wp = iP[1]


wa, wp, step = LineMethod(wa, wp, tolerance, step, inpdata, d)

fwa = wa
fwp = wp
results =[]
results.append([wa, wp])

results = moveLine(wa, wp, step, tolerance, inpdata, d ,results, rangwa = ranges[0], rangwp = ranges[1])

print("Change direction")
wa = fwa
wp = fwp
results = moveLine(wa, wp, -step, tolerance, inpdata, d,results, reverse = True, rangwa = ranges[0], rangwp = ranges[1])


results =  roundR(results)


# os.system("mkdir savedData")
# with open("savedData/rdatapoint.pckl", "wb") as f:
#     pickle.dump(results, f)

results = checkresults(results, inpdata[1:], .5, d)
print(results)
linearregression(d, results, inpdata)
