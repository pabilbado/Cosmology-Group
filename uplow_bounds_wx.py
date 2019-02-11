#import numpy as np
import matplotlib.pyplot as plt
from integrator.trapezium import trapeziumrule as integrate
from functions.t0_part1b import t0_part1b as t0
from numpy import arange
from numpy import abs

#set function
ft = t0()

#set range of w_x values to cycle through
rangwx = [-100,0]

#set step
step = 1e-2

#omega_m values: mean and upper and lower 1-sigma and 2-sigma bounds
Xs = [0.45, 0.25, 0.30, 0.35, 0.40]
#t_0 values: mean and upper and lower 1-sigma and 2-sigma bounds
Ys = [15.0, 10.6, 11.7, 12.8, 13.9]
#statements to show when printing w_x value
meanings = ['2-sigma upper bound: ', '1-sigma lower bound: ', 'Mean: ', '1-sigma upper bound: ', '2-sigma lower bound: ']

#tolerance - how far from the actual answer the calculated answer can be
tolerance = 1e-2

#create text file
text_file = open("wx_values.txt", "w")

#cycle through each bound on omega_m
for i in range(0, len(Xs)):
    #cycle through all w_x values in range
    for wx in arange(rangwx[0], rangwx[1]+step, step):
        #set w_x
        ft.update(wx = wx)
        #calculate value of t_0
        val = ft.cal(Xs[i])
        #print(val)

        #compare calculated value of t_0 to actual value
        if abs(Ys[i]-val) <= tolerance:
            print(meanings[i] + str(wx))
            #print to text file
            text_file.write("%s %f" % (meanings[i], wx) + "\n")
            break

#close text file
text_file.close()
