import pandas as pd
from functions.dCPL import dBAO
db = dBAO()


def datalist(name= "data"):

    d = pd.read_csv('data/{0}.csv'.format(name))   #gets all the data from a csv file from an absolute path to directory.
    df = pd.DataFrame(d)    #obtains dataframe; allows labelled columns and indexed items to be read and passed.
    dfToList = df['z'].tolist() #shifts all the values under the column named z to a list
    z = df["z"].tolist()
    a = df["a"].tolist()
    theta = df["theta"].tolist()
    dic = {"z" : z, "a":a, "theta" : theta}
    return dic

def obtaindata(filename):
    data = datalist(name="{}".format(filename))
    inpdata = []
    for n, z in enumerate(data["z"]):
        inpdata.append([z, db.cal(data["theta"][n])])
    return inpdata
