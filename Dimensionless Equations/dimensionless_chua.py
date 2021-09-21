# Dimensionless Chua Circuit

import math
import sys
import numpy as np

sys.path.append('/home/ashmita/Desktop/ASHMITA/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

import chua_circuit_simulations

#dimensionless chua
R=1.4
C1=1/9
C2=1
L=1/7
Bp=1
m0=-0.5
m1=-0.8

x0=0.1
y0=0.0
z0=0.0
t0=0.0

b0=[x0, y0, z0]

def Yfunc(t,b):
    x,y,z=b
    gx=m0*x+0.5*(m1-m0)*(abs(x+1)-abs(x-1))
    Y=[(1/C1)*((1/R)*(y-x)-gx), (1/C2)*((1/R)*(x-y)+z), (-1/L)*y]
    return Y
    #

h=0.1
N=5000
path="/home/ashmita/Desktop/ASHMITA/NISER Study/7th Semester/Open Lab/Non-Linear Circuit/Dimensionless/"
name=f'dimensionless'
n=path+name
f=open(n, "w")
f.close()
out2=chua_circuit_simulations.RK4_chua(Yfunc,b0,t0,h,N,n)
#
