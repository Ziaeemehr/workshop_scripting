import pandas as pd
import numpy as np 

df = pd.read_csv('ex1.csv')
# print df
# print pd.read_table('ex1.csv', sep=',')
# print pd.read_csv('ex1.csv', header=None)
df.to_csv("out.csv")
