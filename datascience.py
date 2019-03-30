import pandas as pd

#Use pandas csv reader
treeData= pd.read_csv("trees.csv")
print(treeData)
#check that the file looks as it should without printing all data
#df.head() 	df.tail()
#The column names of the datadf.columns
#The column with column name Index
#df[‘Index’]
