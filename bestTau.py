#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:20:41 2017

@author: vittoriobisin
"""

def bestTau(desampleConvolvedNoise,A,bestLamb,realSignal,beta):
    import numpy as np
    from ISTA import ISTA
    
    interval=np.float64(range(-15,10))
    interval=2**interval
    
    best=np.transpose(np.matrix(np.ones(1000)))
    bestTau=1
    
    for tau in interval:
        (estimate,a,b,c)=ISTA(desampleConvolvedNoise,A,bestLamb,realSignal,beta,tau)
        
        if sum(abs(estimate-realSignal))<sum(abs(best-realSignal)):
            best=estimate
            bestTau=tau
            
            
            
            
    return bestTau
