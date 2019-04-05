import numba as nb 
@nb.jit
def _complicated(x):
    return (2*x)

class myClass:
    def __init__(self):
        pass

    def complicated(self,x):                                  
        result = _complicated(x)
        return result

m = myClass()
print m.complicated(10)