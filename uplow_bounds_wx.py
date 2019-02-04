import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from integrator.trapezium import trapeziumrule as integrate
from functions.t0_part1b import t0_part1b as t0
from numpy import arange


ft = t0()

rangwx = [-50,0]
step = 0.01

X = .40
Y = 13.9

tolerance = 1e-3

for wx in arange(rangwx[0], rangwx[1]+step, step):
    ft.update(wx = wx)
    val = ft.cal(X)
    if abs(Y-val) <= tolerance:
        print(wx)
        break

