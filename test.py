from integrator.trapezium import multi as integrate
import math
from functions.parent import Function
from functions.sfq import *

a = dsfq()
print(a.cal(1.0))
a.update(z=2)
print(a.cal(1.0))
