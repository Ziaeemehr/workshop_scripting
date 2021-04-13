#!/usr/bin/python
#http://hplgit.github.io/primer.html/doc/pub/class/._class-readable001.html#sec:class:func2

class Y(object):
    """
    Mathematical function for the vertical motion of a ball.

    Methods:
       constructor(v0): set initial velocity v0.
       value(t): compute the height as function of t.
       formula(): print out the formula for the height.

    Data attributes:
       v0: the initial velocity of the ball (time 0).
       g: acceleration of gravity (fixed).

    Usage:
    >>> y = Y(3)
    >>> position1 = y.value(0.1)
    >>> position2 = y.value(0.3)
    >>> print y.formula()
    v0*t - 0.5*g*t**2; v0=3
    """
    def __init__(self,v0):
        self.v0 = v0
        self.g = 9.81
    def value(self,t):
        return self.v0*t -0.5 * self.g * t*t
    
    def formula(self):
        return 'v0*t-0.5*g*t**2; v0=%g '  % self.v0
    
#print "documentation:", Y.__doc__        
y = Y(3) # v0 = 3
t = 0.1
v = y.value(t) #evalute y(t=0.1,v0=3)
print 'y(t=%g; v0=%g) = %g'% (t,y.v0,v)
print y.formula()


#Another function class example
class V(object):
    def __init__(self,beta,mu0,n,R):
        self.beta,self.mu0,self.n,self.R = beta,mu0,n,R
        
    def value(self,r):
        beta,mu0,n,R = self.beta,self.mu0,self.n,self.R
        n = float(n)
        v = (beta/(2.0*mu0))**(1/n)*(n/(n+1))* \
            (R**(1+1/n) - r**(1+1/n))
        return v
y = V(.1,1.1,.3,.1)
print "class V: ",y.value(50)
print " "

#class Y2(object):
    #def value(self,t,v0=None):
        #if v0 is not None:
            #self.v0 = v0
        #if not hasattr(self,'v0'):
            #print 'You cannot call value(t) without first ' \
                  #'calling value(t,v0) to set v0'
            #return None
        #g = 9.81
        #return self.v0*t-0.5*g*t*t
#Or    
class Y2(object):
    def value(self,t,v0=None):
        if v0 is not None:
            self.v0 = v0
        g = 9.81
        try:
            value = self.v0*t-0.5*g*t*t
        except AttributeError:
            msg = 'You cannot call value(t) without first ' \
                  'calling value(t,v0) to set v0'
            raise TypeError(msg)
        return value
    

y = Y2()
v = y.value(0.1,5)
print y.v0
print v
print y.value(0.2)
    
    





















