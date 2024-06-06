import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

new_data = pd.DataFrame()

values = data['whoAmI'].unique()

for mean in values:
    new_data[mean] = (data['whoAmI'] == mean).astype(int)

print(new_data)