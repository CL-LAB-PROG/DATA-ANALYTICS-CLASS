import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('datanew.csv')

print(df.head())
print(df.describe())

