#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 18:39:09 2017

@author: vittoriobisin
"""


def TwIST(desampleConvolvedNoise,A,tau,lamb,realSignal,alpha,beta):
    import numpy as np
    from TVNorm import TVNorm
    from TV_denoise import TV_denoise
    import scipy.stats

    
    #stopping criterions
    iter=1
    IST_iters=0
    TwIST_iters=0
    for_ever=2
    maxiter=1000
    tau=1000

    x=np.transpose(np.matrix(np.zeros(1000)))
    xm2=x
    xm1=xm2
    mse=list()
    SNR=list()
    SAD=list()
    mse.append(sum(((np.square(x-realSignal))))/np.float64(len(x)))
    SNR.append(scipy.stats.signaltonoise(x))
    SAD.append(sum(abs(x-realSignal)))    

    
    j=1
    i=1
    max_svd=1 
    resid=desampleConvolvedNoise-A*x
    flattenedResid=np.matrix(resid.flatten())
    prev_f=np.matrix.item(.5*(flattenedResid*np.transpose(flattenedResid))+tau*TVNorm(x))
    
    initialResid=resid


## TwIST iteration

    print("i've started")
    while iter < maxiter:
        for_ever=3
        grad=np.transpose(A)*resid
        while for_ever>2:
            j+=1
            
            #Call the shrinkage/denoising function
            x=np.float64(TV_denoise(xm1+grad/max_svd,tau/max_svd))
            
            
            # If not the first TwIST iteration
            if IST_iters>=2 or TwIST_iters>0:
                print("Things are progressing")
                xm2=(alpha-beta)*xm1 +(1-alpha*xm2+beta*x)
                resid=desampleConvolvedNoise-A*xm2
                f=np.matrix.item(.5*(np.transpose(resid.flatten()*np.transpose(resid.flatten()))+tau*TVNorm(x)))
                if f>prev_f:
                    TwIST_iters=0
                else:
                    TwIST_iters=TwIST_iters+1
                    IST_iters=0
                    x=xm2
                    print(i)
                    i+=1
                    for_ever=1
                    break
            #If the first TwIST iteration (procedure of MTwIST)    
            else:
                resid=desampleConvolvedNoise-A*x
                f=np.matrix.item(5*(resid.flatten()*np.transpose(resid.flatten()))+tau*TVNorm(x))

                if f>prev_f:
                    print("f is increasing")
                    max_svd=2*max_svd
                    IST_iters=0
                    TwIST_iters=0
                    
                else:
                    TwIST_iters=TwIST_iters+1
                    print(i)
                    i+=1
                    for_ever=1
                    break
         
        xm2=xm1    
        xm1=x
        iter=iter+1
        print(iter)
        prev_f=f        
        mse.append(sum(((np.square(x-realSignal))))/np.float64(len(x)))
        SNR.append(scipy.stats.signaltonoise(x))
        SAD.append(sum(abs(x-realSignal))) 
        
        return x
       