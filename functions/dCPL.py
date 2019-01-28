from integrator.trapezium import multi as integrate
import math

class dCPLintegrand():
    def __init__(self):
        self.c = 1
        self.a0= 1
        self.H0= 1
        self.omeM = 1
        self.omeX= 1
        self.wp= 1
        self.wa= 1

    def cal(self, x):
        px = math.pow((self.a0/x),(3*(self.wp + self.wa))) * math.exp(3*self.wa * (x/self.a0 - 1 ))

        squarerootpart = math.sqrt(self.omeM + (self.omeX * px))

        integrand = 1./(math.sqrt(x) * squarerootpart)
        return integrand


class dCPL():
    def __init__(self):
        self.c = 1
        self.a0= 1
        self.H0= 1
        self.omeM = 1
        self.omeX= 1
        self.wp= 1
        self.wa= 1


    def cal(self, z):
        az = 1./1+z
        return (self.c / (math.sqrt(self.a0) * self.H0)) * integrate(dCPLintegrand(), [az, self.a0], 0.001)

print(dCPL().cal(0.01))
