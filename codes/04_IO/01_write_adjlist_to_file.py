import numpy as np     
import networkx as nx 

#--------------------------------------------------------#    
def adjmat_to_adjlist(adjmat, threshold=1e-5):
        '''
        gets adjmat as nd array
        return adjlist as list of list
        '''
        adjmat = np.asarray(adjmat)
        row, col = adjmat.shape
        adjlist = []

        for i in range(row):
            neighbours = [i]
            for j in range(col):
                if (adjmat[i,j] >threshold):
                    neighbours.append(j)
            adjlist.append(neighbours)
        
        return adjlist
#--------------------------------------------------------#    
def write_adjlist(adjlist, fname):
    '''
    write adjlist to file
    '''
    nodes = len(adjlist)

    f = open('data/a.adjlist', 'w')
    for i in adjlist:
        for j in i:
            f.write('%d\t' % j);
        f.write('\n')
    f.close()


#--------------------------------------------------------#    

if __name__ == "__main__":
    

    G = nx.erdos_renyi_graph(10, 0.5, seed=1253)
    adjmat = nx.to_numpy_array(G, dtype=int)
    print adjmat
    
    adjlist = adjmat_to_adjlist(adjmat)
    for i in adjlist:
        print i
    
    write_adjlist(adjlist, 'a2.adjlist')

