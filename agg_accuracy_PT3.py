import math
from functions.d_lambdaCDM import dCDM
from functions.dL_PartIII import dL as dDGP

#create luminosity distance functions
dDGP = dDGP()
dCDM = dCDM()

#redshifts at which to calculate aggregate accuracy
z1 = 0.5
z2 = 1.32

#assign appropriate values in luminosity distance functions for Lambda-CDM models
#dCDM.update(factor=0)

#calculate d_L for each model at redshift z=0.5
d_L = dDGP.cal(z1)
print(d_L)
d_lamcdm = dCDM.cal(z1)
print(d_lamcdm)
#find aggregate accuracy for DGP model
aggy1 = math.abs((d_L1-d_lamcdm)/d_L)
print('sfq1 (z = ' + z1 + '):' + aggy1)

#calculate d_L for each model at redshift z=1.32
d_L = dDGP.cal(z1)
d_lamcdm = dCDM.cal(z1)
#find aggregate accuracy for DGP model
aggy1 = math.abs((d_L1-d_lamcdm)/d_L)
print('sfq1 (z = ' + z2 + '):' + aggy1)
