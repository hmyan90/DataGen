import pandas as pd
import glob

#df = pandas.read_csv("/home/hyan90/Documents/download/data/b.csv", sep=';')
#print df

#new_data = pds.DataFrame()
#df[['object_id', 'message']].drop_duplicates(subset='object_id').to_csv("/home/hyan90/Documents/download/data/22.csv")



path ="/home/hyan90/Documents/download/data" # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, sep=';')[['object_id', 'message']]
    list_.append(df)
frame = pd.concat(list_)
frame.drop_duplicates(subset='object_id').to_csv("/home/hyan90/Documents/download/data/22.csv")
