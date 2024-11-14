import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips= sns.load_dataset('tips')

df = pd.DataFrame(tips)
print (df.head(11))