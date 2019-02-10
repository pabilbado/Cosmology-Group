import pandas as pd
from functions.dCPL import dBAO, dCPL
import numpy as np


def Generatetest(wa, wp, f = dCPL(), dbao = dBAO()):
    f.update(wa= wa, wp = wp)
    dic = {"z":[], "theta":[], "a":[]}
    for z in np.arange(0.1,2.1,.1):
        dic["z"].append(z)
        dic["theta"].append(dbao.cal(f.cal(z)))
        dic["a"].append(1/(1+z))
    df = pd.DataFrame(dic)
    print(df)
    df.to_csv("data/data_test.csv")
