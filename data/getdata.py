import pandas as pd


def datalist():

    d = pd.read_csv('data/data.csv')   #gets all the data from a csv file from an absolute path to directory.
    df = pd.DataFrame(d)    #obtains dataframe; allows labelled columns and indexed items to be read and passed.
    dfToList = df['z'].tolist() #shifts all the values under the column named z to a list
    z = df["z"].tolist()
    a = df["a"].tolist()
    theta = df["theta"].tolist()
    dic = {"z" : z, "a":a, "theta" : theta}
    return dic
