from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing

from numpy import arange as int_points
import math


def simpsrule(f, rang, step):
    # Set the integration limits
    if rang[0] < rang[1]:
        lowX = rang[0]
        upX = rang[1]
        var = 1.
    else:
        lowX = rang[1]
        upX = rang[0]
        var = -1.
    # Makes sure n is even
        n = (upX - lowX)/step
        if n%2 != 0:
            n += 1
            step = (upX - lowX)/n

    first = True
    second = False
    value = 0
    for x_3 in int_points(lowX, upX, step):

        if first:
            x_1 = x_3
            first = False
            second = True

        if second:
            x_2 = x_3
            second = False
        else:
            value += (step/6)*(f.cal(x_1)+ 4*f.cal(x_2) + f.cal(x_3))
            x_1 = x_2
            x_2 = x_3


    return value*var

class f():
    def cal(self, x):
        return x*x




"""
Multi method: This method executes the trapeziumrule by breaking the integral into the number of CPUS to improve efficiency.
              Inputs:
              | *f is the function to integrate, it must be an object with a callable method cal(x) that will output f(x)
              | *rang [lowX, upX] is the upper and lower limits to integrate
              | *step this is the delta between integration steps

              Outputs:
              | * the resulting value of the integration
"""

def multi(f, rang, step, free =1):
    if rang[0] < rang[1]:
        lowX = rang[0]
        upX = rang[1]
        var = 1.
    else:
        lowX = rang[1]
        upX = rang[0]
        var = -1.
    Ncpu = (multiprocessing.cpu_count()-free)            # Obtain the number of CPUS
    fstep =  (rang[1]-rang[0]) / Ncpu                    # Calculate the range each CPU is going to run


    pool = Pool(Ncpu)                                    # Create a pool of Ncpu workers
    arg = []                                             # Initialize the argument list for each process
    for n in range(1, Ncpu+1):
        Frang = [rang[0]+ (n-1)*fstep ,rang[0]+n*fstep]  # The range of integration for each CPU
        arg.append((f, Frang, step))                     # Create the list of arguments with different ranges

    results = pool.starmap(simpsrule, arg)           # Using the trapezium rule to map each argument to a result
    pool.terminate()
                                                         ## space giving a list of integration results

    result = 0                                           # Set the result value to 0
    for val in results:                                  # Sum over all the results outputted by the different processes
        result += val

    return result * var                                  # Return final result
