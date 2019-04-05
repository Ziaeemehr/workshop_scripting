import pandas as pd 
import numpy as np 

x = [0.1, 0.2]
y = [1, 2]
data = [[{'x11': [1, 2, 3]},
         {'x12': [1, 2, 3]}],
        [{'x21': [1, 2, 3]},
         {'x22': [1, 2, 3]}]]
frame2 = pd.to_pickle(data, "t.pkl")
data2 = pd.read_pickle("t.pkl")
print data2[0][0]

