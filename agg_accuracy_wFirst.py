import math
from functions.sfq import dsfq

#create luminosity distance functions
dsfq1 = dsfq()
dsfq2 = dsfq()
dcdm = dsfq()

#redshifts at which to calculate aggregate accuracy
z1 = 0.5
z2 = 1.32

#assign appropriate values in luminosity distance functions for SFQ-I, SFQ-II and Lambda-CDM models
dsfq1.update(factor=1, at=0.50, tau=0.33, wp=0, wm=0, wf=-1)
dsfq2.update(factor = 1, at=0.23, tau=0.33, wp=0, wm=0, wf=-1)
dcdm.update(factor=0)

#calculate d_L for each model at redshift z=0.5
d_L1 = dsfq1.cal(z1)
d_L2 = dsfq2.cal(z1)
d_lamcdm = dCDM.cal(z1)
#find aggregate accuracy for SFQ-I model
aggy1 = math.abs((d_L1-d_lamcdm)/d_L1)
print('sfq1 (z = ' + z1 + '):' + aggy1)
#find aggregate accuracy for SFQ-I model
aggy2 = math.abs((d_L2-d_lamcdm)/d_L2)
print('sfq2 (z = ' + z1 + '):' + aggy2)

#calculate d_L for each model at redshift z=1.32
d_L1 = dsfq1.cal(z2)
d_L2 = dsfq2.cal(z2)
d_lamcdm = dCDM.cal(z2)
#find aggregate accuracy for SFQ-I model
aggy1 = math.abs((d_L1-d_lamcdm)/d_L1)
print('sfq1 (z = ' + z2 + '):' + aggy1)
#find aggregate accuracy for SFQ-II model
aggy2 = math.abs((d_L2-d_lamcdm)/d_L2)
print('sfq2 (z = ' + z2 + '):' + aggy2)
