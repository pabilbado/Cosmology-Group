from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing

from numpy import arange as int_points
import math


"""
Example function to integrate: must have a cal(x) which outputs f(x)
"""

class example:

    # Compulsory initialize method
    def __init__(self):
        pass

    # cal method that returns outputs the f(x)
    def cal(x):
        return x*x + x*x*x +math.exp(- x*x)


"""
Trapezium Rule: This function| *calculates the integral given| *a function object (It must contain a method cal(x) that outputs the value f(x))
                             |                               | *a range [lowX, upX] (lowX lower integration range, and upX is the upper integration range)
                             |                               | *a step (this is the step or delta between integration steps)
                             |
                             | *outputs a float value which is the result of the integration
"""

def trapeziumrule(f, rang, step):
    # Set the integration limits
    if rang[0] < rang[1]:
        lowX = rang[0]
        upX = rang[1]
        var = 1.
    else:
        lowX = rang[1]
        upX = rang[0]
        var = -1.

    # Preliminary settings
    first = True          # Setting the first flag as True to start calculating from value x1 instead of x0
    value = 0             # Initialise the result of the integration
    prevX = lowX          # Sets the x_(0) to the initial value of integration



    for x in int_points(lowX, upX, step):

        # If first iteration then it skips it in order to start at x1, not x0
        if first:
            prevX = x                                     # Sets x_(0) to the first x value
            first = False                                 # Disables the first flag trigger

        # If it is not the first iteration
        else:
            value += (f.cal(prevX) + f.cal(x))/2 * step   # Use the trapezium rule to calculate the term in the sum and add it to the total sum
            prevX = x                                     # Set the x_(n-1) to the current x for the next iteration

    value += (f.cal(prevX) + f.cal(upX))/2 * step         # Add the final term which is not accounted in the for Loop
    return value * var                                     # return the final value





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
    Ncpu = multiprocessing.cpu_count()-free              # Obtain the number of CPUS
    fstep =  (rang[1]-rang[0]) / Ncpu                    # Calculate the range each CPU is going to run


    pool = Pool(Ncpu)                                    # Create a pool of Ncpu workers
    arg = []                                             # Initialize the argument list for each process
    for n in range(1, Ncpu+1):
        Frang = [rang[0]+ (n-1)*fstep ,rang[0]+n*fstep]  # The range of integration for each CPU
        arg.append((f, Frang, step))                     # Create the list of arguments with different ranges

    results = pool.starmap(trapeziumrule, arg)           # Using the trapezium rule to map each argument to a result
    pool.terminate()
                                                         ## space giving a list of integration results

    result = 0                                           # Set the result value to 0
    for val in results:                                  # Sum over all the results outputted by the different processes
        result += val

    return result * var                                  # Return final result
