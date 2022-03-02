import pandas as pd
import numpy as np

data = {'race': [11, 0, 2, 3, 0, 1],
        'rate': np.random.rand(6)*10}


df = pd.DataFrame(data=data)
print(df)

df = df[df.race !=0]

print(df)
