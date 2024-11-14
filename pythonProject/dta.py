import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_excel('accountss.csv')

#check for missinf values or components
print(df.isnull().sum())

#fill missing values with a specific value
df.fillna(value=0, inplace=True)

#drop rows with missing values
df.dropna(inplace=True)

#drops/deletes all the duplicates
df.drop_duplicates(inplace=True)