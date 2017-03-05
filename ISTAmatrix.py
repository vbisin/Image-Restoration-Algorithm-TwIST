#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:36:31 2017

@author: vittoriobisin
"""

def ISTAmatrix(desampleConvolvedNoise,A,lamb,realSignal,beta,tau):
    import numpy  as np 
    from TV_denoise import TV_denoise
    import scipy.stats

    
    
    xOld=np.transpose(np.matrix(np.zeros(1000)))
    mse=list()
    SNR=list()
    SAD=list()
    matrix=np.zeros((1000,20))
    
        
    for j in range(0,20):
        resid=desampleConvolvedNoise-A*xOld
        grad=np.transpose(A)*resid
        psi=np.float64(TV_denoise(xOld+grad,tau))
        xNew=(1-beta)*xOld+beta*psi
        mse.append(sum(((np.square(xNew-realSignal))))/np.float64(len(xNew)))
        SNR.append(scipy.stats.signaltonoise(xNew))
        SAD.append(sum(abs(xNew-realSignal)))
        xOld=xNew    
        a=np.array(xOld)
        matrix[:,j]=np.asarray(np.squeeze(a))
              
        
    
    return (xOld,mse,SNR,SAD,matrix)