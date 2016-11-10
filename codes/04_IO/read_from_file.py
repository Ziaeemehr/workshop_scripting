import numpy as np
def read_from_file(filename):
    """
    Generate lists using data from file.
    
    :param file:
    :return:
    """
    #file = "data.txt"
    with open(filename, "r") as datafile:
        data = datafile.read().split()
        dates = data[:,0]
        rates = data[:,1]
        data_array = np.asarray(data)
        dates_a = np.asarray(dates)
        rates_a = np.asarray(rates)
        print data_array.shape, dates_a.shape, rates_a.shape
    #for i in range(len(dates)):
        #print rates[i],dates[i]
        #print len(dates), len(rates)
    
read_from_file("data.txt")    
