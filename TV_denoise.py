#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 18:38:22 2017

@author: vittoriobisin
"""
def TV_denoise(x, lamb):
    import numpy as np
    import matplotlib.pyplot as plt

    ## I want iu (ir) and id (il)
    tv_iterations=15
    dt=.25
    N=len(x)
    
    
    #Our signal is a vector
    id=np.zeros(x.shape)
    id[:,0]=np.arange(len(x))
    id[:]=id[:]+2
    id[N-1]=id[N-2]
    
    
    #creating iu
    iu=np.arange(N)
    iu[0]=iu[1] 
    iu=np.transpose(np.matrix(iu))

    p2=np.zeros(x.shape)
    z2=np.zeros(x.shape)
    divp=np.zeros(x.shape)
    zModified=np.zeros(x.shape)
    p2Modified=np.zeros(x.shape)

    
    
    #iteration of TV_denoise
    for i in range(1,tv_iterations):
        z=divp-x*lamb
        
        #creating z1
        for j in range(0,N):
            zModified[j]=z.item(np.int(id[j]-1))
        
        z2=zModified-z
        

        denom=1+dt*np.sqrt(np.square(z2))
        p2=np.divide(p2+dt*z2,denom)
        
        #creating divp
        for j in range(0,N):
            p2Modified[j]=p2.item(np.int(iu[j]-1))
        divp=p2-p2Modified
        
    u=x-divp/lamb   
    
    return u
        
       # il with  and ir we replace 
