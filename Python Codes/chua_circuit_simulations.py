#Chua circuit simulations

import math
import handling_files
import numpy as np

#RK4 to solve Chua circuit equations (a system of 3-ODEs)
def RK4_chua(F,b,t,h,N,name):
    handling_files.append_file(name, f'{t} {b[0]} {b[1]} {b[2]}\n')
    for i in range(N):
        K1=F(t,b)
        #
        K2=F(t+h/2, b+np.multiply(K1,h/2))
        #
        K3=F(t+h/2, b+np.multiply(K2,h/2))
        #
        K4=F(t+h, b+np.multiply(K3,h))
        #
        b=b+np.multiply((K1+np.multiply(K2,2)+np.multiply(K3,2)+K4), h/6)
        t=t+h
        handling_files.append_file(name, f'{t} {b[0]} {b[1]} {b[2]}\n')
        #
    return(1)


