#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:04:03 2017

@author: vittoriobisin
"""

def denoiseCheck (realSignal):
    
    import numpy as np
    from TV_denoise import TV_denoise
    # Add noise to this signal
    noisy=realSignal+ np.transpose(np.matrix(np.random.normal(0,1,1000)))
    interval=np.float64(range(-15,10))
    interval=2**interval
    best=np.transpose(np.matrix(np.ones(1000)))
    bestLamb=1
    
    for i in interval:   
        denoised=TV_denoise(noisy,i)
        if np.matrix.sum(np.abs(best-realSignal))>np.matrix.sum(np.abs(denoised-realSignal)):
            best=denoised
            bestLamb=i
            
            
    return bestLamb

    