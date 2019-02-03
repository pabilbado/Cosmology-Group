import integrator.trapezium as multi
from data.getdata import data_as_list
from functions.sfq import *


initsfq = sfq_integral()  #initiates the sfq_integral class from sfq.py module.
print(initsfq.cal())  #prints out the integral from sfq.py module.
# initdata = data_as_list()
# print(initdata.datalist())
