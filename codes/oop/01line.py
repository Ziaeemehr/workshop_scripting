class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
        
    def __call__(self, x):
        return self.c0 + self.c1*x
    def table(self, L, R, n):
        '''Return a table with n points for L <= x <= R. '''
        s = ''
        import numpy as np
        for x in np.linspace(L,R,n):
            y = self(x)
            s += '%12g %12g \n' %(x,y)
            return s
        
        
class Parabola:
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
        
    def __call__(self, x):
        return self.c2*x*x + self.c0 + self.c1*x
    
    def table(self, L, R, n):
        '''Return a table with n points for L <= x <= R. '''
        s = ''
        import numpy as np
        for x in np.linspace(L,R,n):
            y = self(x)
            s += '%12g %12g \n' %(x,y)
            return s
        
                