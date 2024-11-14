import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns



df= pd.read_csv('accountss.csv')

print (df.head(20))
print (df.describe())


print (df.dtypes)

sns.pairplot(df)
plt.show()