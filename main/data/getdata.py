import pandas as pd

class data_as_list():

    def datalist(self):

        d = pd.read_csv('~/Cosmology-Group/main/data/data.csv')   #gets all the data from a csv file from an absolute path to directory.
        df = pd.DataFrame(d)    #obtains dataframe; allows labelled columns and indexed items to be read and passed.
        dfToList = df['z'].tolist() #shifts all the values under the column named z to a list
        return dfToList
