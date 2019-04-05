# HH model with various Stimulation current 
# output:  plot t-V
#          plot m,n,h -t
#          plot V-n 

import numpy as np
import matplotlib.pylab as plt
from scipy.integrate import odeint
from math import *
from sys import exit

#constants----------------------------------------------------
gbar_Na= 120;        #(micro A/mV)/cm^2
gbar_K= 36;          #(micro A/mV)/cm^2
gbar_L= 0.3;         #(micro A/mV)/cm^2
E_Na= 50.0;          #mV
E_K = -77.0;         #mV
E_L = -54.6;         #mv
C = 1.0;             #micro F/cm^2

#-------------------------------------------------------------
def coefficients(v):
    alph_n  = 0.01*(v + 55.0)/(1.0 - exp(-(v + 55.0)/10.0))
    beta_n  = 0.125*exp(-(v +65.0)/80.0)
    alph_m  = 0.1*(v + 40.)/(1-exp(-(v + 40.0)/10.0))
    beta_m  = 4.0*exp(-(v + 65.0)/18.0)
    alph_h  = 0.07*exp(-(v + 65.0)/20.0)
    beta_h  = 1.0/(1.0 + exp(-(v + 35.0)/10.0))
    J = [alph_m,beta_m,alph_n,beta_n,alph_h,beta_h]
    return J
#-------------------------------------------------------------    
def initialize():
    x = [0., 0., 0., 0.]
    x[0] = -65.0;                              #V
    J = coefficients(x[0]);                        
    alph_m,beta_m,alph_n,beta_n,alph_h,beta_h = J
    x[1] = alph_m /(alph_m + beta_m);          #m
    x[2] = alph_n /(alph_n + beta_n);          #n
    x[3] = alph_h /(alph_h + beta_h);          #h
    return x
#-------------------------------------------------------------
def xpsys(x,t,Isti):
    # u_dot(u,m,n,h) u,m,n,h -> 0,1,2,3
    J = coefficients(x[0])
    alph_m,beta_m,alph_n,beta_n,alph_h,beta_h = J
    vp = -(gbar_Na* x[1]**3 * x[3]*(x[0]-E_Na)+ \
    gbar_K * x[2]**4 *(x[0]-E_K) + \
    gbar_L * (x[0]-E_L)) + Isti                         #V dot
    mp = alph_m * (1-x[1])- beta_m * x[1]               #m dot
    np = alph_n * (1-x[2])- beta_n * x[2]               #n dot
    hp = alph_h * (1-x[3])- beta_h * x[3]               #h dot
    return vp,mp,np,hp
#-------------------------------------------------------------

# plot V vs. n
def plot_pplane(I,fignum=3):
    plt.figure(fignum)
    #plt.clf()
    plt.xlabel('Voltage(mV)')
    plt.ylabel('n')
    plt.xlim([-80,80])
    plt.ylim([0.3,0.8])
    plt.plot(sol[:,0],sol[:,2],label='I= '+str(I))
    plt.legend(frameon=False, prop={'size':10})
    
#-------------------------------------------------------------
t0 = 0.0
tn = 30.0
t = np.linspace(t0,tn,num=1000)
x = initialize()
Isti =  np.arange(6.,6.4,0.1)
Isti = np.append(Isti,[9.,9.1,20,100])

for I in Isti :
    sol = odeint(xpsys,x,t,args=(I,))
    plot_pplane(I)

plt.savefig('phase.png')

#ploting----------------------------------------------------
#plt.figure()
#plt.plot(t,sol[:,0],'-',label='Voltage')
#legend = plt.legend(loc='upper right', frameon=False)
#plt.xlabel('time(ms)')
#plt.savefig('./results/V.png')
#plt.figure()
#plt.plot(t,sol[:,1],'-',label='m')
#plt.plot(t,sol[:,2],'-',label='n')
#plt.plot(t,sol[:,3],'-',label='h')
#legend = plt.legend(loc='upper left', frameon=False)
#plt.xlabel('time(ms)')
#plt.savefig('./results/nmh.png')
#plt.show()
#-------------------------------------------------------------

