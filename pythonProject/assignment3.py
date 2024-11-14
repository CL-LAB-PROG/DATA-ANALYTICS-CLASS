import pandas as pd 

df= pd.read_csv('employees.csv')

print (df.head(20))

print (df.isnull().sum()) 

print (df.loc [0:10, 'First Name'])






