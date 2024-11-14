import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {'students': ["cliff", "allison","abiye","mira","jason" ],
        'courses': ["public health","anatomy","engineering","law","physiology"]
        
        }

df= pd.DataFrame(data)

plt.bar(df ["students"], df ["courses"])

plt.xlabel("students")
plt.ylabel("courses")
plt.show()