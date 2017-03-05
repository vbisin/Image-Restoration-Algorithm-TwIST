#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:40:47 2017

@author: vittoriobisin
"""
# Uses a Hann window to smooth given signal and then adds random noise N(0,1)
# then de-samples and takes 1 out of 5 samples

def blur (t,realSignal):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import scipy.ndimage.filters
    from extra import convmtx
    from kernel import gauss
    ##Smoothing the signal using a Hann window
    #window = signal.hann(1000)
    #signal.convolve(s, window, mode='same') / sum(window)
    
        
    #Correct Gaussian Kernel 
    gaussian=gauss(100,10)
    gaussian=gaussian[1:len(gaussian)]
    

    #Get gauss filter 
    
    

    #Solving bam via convmtx
    bam=convmtx(gaussian,1000)
    bam=bam[:,50:1050]
    #bam=np.concatenate((bam[:,50:1000],bam[:,1000:1500]),1)
    bam=np.matrix(bam)
    blurMatrix=np.zeros((200,1000))
    for i in range(0,200): 
       blurMatrix[i,:]=bam[5*i,:]
    
    

    #Blurring with Gaussian Filter     
    desampleConvolved = blurMatrix*realSignal
    
    desampleTime=np.zeros(200)    
    desampleRealSignal=np.zeros(200)
    for i in range(0,200):
        desampleTime[i]=t[i*5]
        desampleRealSignal[i]=realSignal[i*5]
    desampleRealSignal=np.transpose(np.matrix(desampleRealSignal))

    
    # Set BSNR
    #BSNR=40
    #Py=np.var(blurMatrix)
    #sigma=math.sqrt(Py/10**(BSNR/10))
    sigma=1
    ## Adding noise
    desampleConvolvedNoise=np.zeros(200)
    noise = np.transpose(np.matrix(np.random.normal(0,1,200)))
    desampleConvolvedNoise = desampleConvolved + sigma*noise
    
    convolvedNoise=bam*realSignal+np.transpose(np.matrix(np.random.normal(0,1,1000)))
#    
#   
#
#     
    
    return (desampleConvolvedNoise,blurMatrix,gaussian,sigma,convolvedNoise,desampleConvolved)
    
    
  #  blurMatrix=np.zeros((200,1000))
    #Code to convolve matrix so output is a 200 vector
   # for i in range(0,200):
    #    gauss=scipy.ndimage.filters.gaussian_filter1d(identity,1)
     #   v=np.zeros(1000)
      #  if i*5<=500:
       #     v[5*i:5*i+500]=gauss[500:]
        #    v[:5*i]=gauss[500-5*i:500]
         #   blurMatrix[i]=v

        #else:
         #   v=blurMatrix[200-i]
          #  blurMatrix[i]=np.fliplr([v])[0]
        
       # blurMatrix=np.matrix(blurMatrix)
        #blurMatrix=np.fft.fftshift(blurMatrix)
        #blurMatrix=blurMatrix/np.matrix.sum(blurMatrix)
                      
                      
        #v[500+5*i:]=np.zeros(500-5*i)
        #a=gauss[5*i:500] 
        #v[5*i:500]=a[::-1]
        
        #v[0:5*i]=gauss[500:5*i]
        #blurMatrix[i]=v

   # convolved=np.convolve(s,gauss,'same')
    #desampleTime=np.zeros(200)
    #desampleConvolved=np.zeros(200)
    
    #for i in range(0,200):
     #   desampleConvolved[i]=convolved[i*5]
      #  desampleTime[i]=t[i*5]


    
    
    #Blur operator like in TwIST code
   # BlurMatrix=np.zeros((200,1000))
    #blur x size
    #for i in range(97,105):
     #   for j in range(497,505):
      #      BlurMatrix[i,j]=1
    #BlurMatrix=np.fft.fftshift(BlurMatrix)
    #BlurMatrix=np.matrix(BlurMatrix)
    #BlurMatrix=BlurMatrix/np.matrix.sum(BlurMatrix)
    
   # lhs=np.matrix(np.fft.fft2(BlurMatrix))
    #rhs=np.matrix(np.fft.fft(s))
    #rhs=np.transpose(rhs)
    
    #convolved=np.real(np.fft.ifft(lhs*rhs));
           
 
##  Gaussian kernel code
# gauss = Gaussian2DKernel(15,x_size=1000,y_size=200)
#gauss=np.matrix(gauss)
#realSignal=np.transpose(np.matrix(realSignal))
#estimate=gauss*realSignal

    