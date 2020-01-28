import pandas as pd
import numpy as np 
# names=['source','target']
# df = pd.read_excel (r'DAG1srcwith10Loop-SF-0.xls', header=None,names=names) 
# print (df)

def adjListToAdjMatrix(adjList, N):
    
    adjMat = np.zeros((N, N), dtype=int)

    row = adjList.shape[0]
    for i in range(row):
        for j, k in [adjList[i, :]]:
            adjMat[j, k] = 2

    return adjMat


fileName = "DAG1srcwith10Loop-SF-0"
df = pd.read_excel(fileName +'.xls', 
                #    sheet_name ='Data_sheet', 
                   header=None, 
                   index_col=False)

N = 1000
adjList = df.to_numpy()
# print (type(adjList[0][0]))
adjMatrix = adjListToAdjMatrix(adjList, N)
np.savetxt(fileName + ".txt", adjMatrix, fmt="%d")