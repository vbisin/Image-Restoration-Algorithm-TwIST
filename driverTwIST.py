#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from TwIST import TwIST
from blur import blur
from CheckDeNoising import denoiseCheck
from ISTA import ISTA
from TV_denoise import TV_denoise
from bestTau import bestTau
## Setting up signal 

# Sampling frequency     
Fs = 1000.0
# Sampling period                            
T = 1.0/Fs           
# Time vector
t= np.zeros(1000)
for i in range (0,1000):
    t[i]=(i*T)    

    

## Real signal: step function 
realSignal=np.zeros(1000)
realSignal[0:100]=0
realSignal[100:200]=20
realSignal[200:300]=30
realSignal[300:400]=40
realSignal[400:600]=50
realSignal[600:700]=70        
realSignal[700:800]=80
realSignal[800:1000]=100
        
desampleTime=np.zeros(200) 
desampleRealSignal=np.zeros(200)       
realSignal=np.transpose(np.matrix(realSignal))    
for i in range(0,200):
    desampleTime[i]=t[i*5]    
    desampleRealSignal[i]=realSignal[i*5]


#Signal: sinusoid1 50 Hz, amplitude 0.7 ; sinudois2 120 Hz, amplitude1 
#s=np.zeros(1000)
#for i in range (0,999):
 #   s[i]=(0.7*math.sin(2*math.pi*50*t[i]) + math.sin(2*math.pi*120*t[i]))


##Blur it
(desampleConvolvedNoise,A,kernel,sigma,convolvedNoise,desampleConvolved) = blur(t,realSignal)
desampleRealSignal=np.transpose(np.matrix(desampleRealSignal))
onlyNoisy=desampleRealSignal+np.transpose(np.matrix(np.random.normal(0,1,200)))

        

# TwIST parameters

#Empirical setting for smoothing parameter, tau
#tau = 2*math.e**-2*sigma/(0.56**2)
#lamb=1e-4;
    # TwIST is not very sensitive to this parameter
    # rule of thumb: lam1=1e-4 for severyly ill-conditioned% problems
    #              : lam1=1e-1 for mildly  ill-conditioned% problems
    #              : lam1=1    when A = Unitary matrix





#bestLamb=denoiseCheck(realSignal)
bestLamb=.5
u=TV_denoise(onlyNoisy,bestLamb)


bestBeta=(2./(1.+bestLamb))

#optTauIST=2
#optTauISTopt=2
optTauIST=bestTau(desampleConvolvedNoise,A,bestLamb,realSignal,1)
optTauISTopt=bestTau(desampleConvolvedNoise,A,bestLamb,realSignal,bestBeta)

(recoveredIST,mseIST,SNRIST,SADIST)=ISTA(desampleConvolvedNoise,A,bestLamb,realSignal,1,optTauIST)
(recoveredISTopt,mseISTopt,SNRISTopt,SADISTopt)=ISTA(desampleConvolvedNoise,A,bestLamb,realSignal,bestBeta,optTauISTopt)

#from ISTAmatrix import ISTAmatrix
#(recoveredIST,mseIST,SNRIST,SADIST,matrixIST)=ISTAmatrix(desampleConvolvedNoise,A,bestLamb,realSignal,1,optTauIST)
#
#plt.figure(1)
#line1=plt.plot(t,matrixIST[:,0],'r',label='1')
#line1=plt.plot(t,matrixIST[:,5],'b',label='2')
#line1=plt.plot(t,matrixIST[:,10],'g',label='3')
#line1=plt.plot(t,matrixIST[:,15],'p',label='4')
#line1=plt.plot(t,matrixIST[:,19],'h',label='5')
#plt.legend(bbox_to_anchor=(.72, .99), loc=0, borderaxespad=0.)
#plt.title("Evolving ISTA")
#plt.savefig('Evolving ISTA')
#plt.show







## Graphs

plt.figure(1)
line1=plt.plot(t,realSignal,'r',label='Original Signal')
line3=plt.plot(desampleTime,desampleConvolvedNoise,'b',label='Desampled Convolved Signal with Noise')
plt.legend(bbox_to_anchor=(.72, .99), loc=0, borderaxespad=0.)
plt.title("Original and Convolved Noisy Signals")
plt.savefig('Original and Convolved Noisy Signals')
plt.show



plt.figure(2)
line1=plt.plot(t,realSignal,'r',label='Original Signal')
line2=plt.plot(t,recoveredIST,'k',label='Recovered Signal')
plt.legend(bbox_to_anchor=(.37, .99), loc=0, borderaxespad=0.)
plt.title("Original and Recovered Signals")
plt.savefig('Original and Recovered Signals')
plt.show



plt.figure(3)
line1=plt.plot(t,realSignal,'r',label='Original Signal')
line2=plt.plot(desampleTime,onlyNoisy,'b',label='Signal with Noise')
plt.legend(bbox_to_anchor=(.37, .99), loc=0, borderaxespad=0.)
plt.title("Original and Noisy Signals")
plt.savefig('Original and Noisy Signals')
plt.show


plt.figure(4)
line1=plt.plot(t,realSignal,'r',label='Original Signal')
line2=plt.plot(desampleTime,u,'b',label='Denoised Signal')
plt.legend(bbox_to_anchor=(.37, .99), loc=0, borderaxespad=0.)
plt.title("Original and Denoised Signals")
plt.savefig('Original and Denoised Signals')
plt.show



plt.figure(5)
line1=plt.plot(t,np.asarray(recoveredIST),'r',label='IST')
line2=plt.plot(t,np.asarray(recoveredISTopt),'b',label='Optimal IST')
plt.legend(bbox_to_anchor=(.3, .99), loc=0, borderaxespad=0.)
plt.title("Recovered Signal via IST and IST Optimal")
plt.savefig('Recovered Signal via IST and IST Optimal')
plt.show


## MSE Error Graphs 
preimage=np.arange(250)


plotMEist=np.zeros(250)
plotMEistopt=np.zeros(250)
plotSNRIST=np.zeros(250)
plotSNRISTopt=np.zeros(250)
plotSADIST=np.zeros(250)
plotSADISTopt=np.zeros(250)


for i in range(0,250):
    plotMEist[i]=mseIST[i].item()
    plotMEistopt[i]=mseISTopt[i].item()
    plotSNRIST[i]=SNRIST[i].item()
    plotSNRISTopt[i]=SNRISTopt[i].item()
    plotSADIST[i]=SADIST[i].item()
    plotSADISTopt[i]=SADISTopt[i].item()




plt.figure(7)
line1=plt.plot(preimage,plotMEist,'r',label='IST')
line2=plt.plot(preimage,plotMEistopt,'b',label='Optimal IST')
plt.legend(bbox_to_anchor=(.18, .99), loc=0, borderaxespad=0.)
plt.xlabel('Iterations')
plt.ylabel('MSE')
plt.title("MSE of IST and IST Optimal Algorithms")
plt.savefig("MSE of IST and IST Optimal Algorithms")
plt.show


plt.figure(8)
line1=plt.plot(preimage,plotSNRIST,'r',label='IST')
line2=plt.plot(preimage,plotSNRISTopt,'b',label='Optimal IST')
plt.legend(bbox_to_anchor=(.98, .98), loc=0, borderaxespad=0.)
plt.xlabel('Iterations')
plt.ylabel('SNR')
plt.title("SNR of IST and IST Optimal Algorithms")
plt.savefig("SNR of IST and IST Optimal Algorithms")
plt.show


plt.figure(9)
line1=plt.plot(preimage,plotSADIST,'r',label='IST')
line2=plt.plot(preimage,plotSADISTopt,'b',label='Optimal IST')
plt.legend(bbox_to_anchor=(.98, .98), loc=0, borderaxespad=0.)
plt.xlabel('Iterations')
plt.ylabel('Sum of Absolute Differences')
plt.title("SAD of IST and IST Optimal Algorithms")
plt.savefig("SAD of IST and IST Optimal Algorithms")
plt.show




## Initilizize x0 randomly
#dummy=np.zeros(1000)
#x0=np.random.normal(dummy);
#x0=np.transpose(np.matrix(x0))


## Run TwIST Iterations

#Max eigenvalues of A'A
#maxEigen=np.max(np.linalg.eigvals(np.matrix(np.transpose(A))*np.matrix(A)))




# I) IST 
#alpha=1
#beta=1

#twistSignal,twistTimes,twistMSE = TwIST(desampleConvolved,A, tau,lamb, realSignal,x0,stoppingThreshold,alpha,beta)
 

#II) ISTopt
#alpha=1
#beta=2/(1+lamb)    

#twistSignal,twistTimes,twistMSE = TwIST(desampleConvolved,A, tau,lamb, realSignal,x0,stoppingThreshold,alpha,beta)

    
#III) TwIST    
#alpha=(1-np.sqrt(lamb))/(1+np.sqrt(lamb))+1
#beta=2*alpha/(1+lamb)
#twistSignal,twistTimes,twistMSE = TwIST(desampleConvolved,A, tau,lamb, realSignal,x0,stoppingThreshold,alpha,beta)










