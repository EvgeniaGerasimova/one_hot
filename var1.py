import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

for mean in data['whoAmI'].unique():
    data[mean] = data['whoAmI'].apply(lambda x: 1 if x == mean else 0)

data = data.drop('whoAmI', axis=1)

print(data)

data.head()
