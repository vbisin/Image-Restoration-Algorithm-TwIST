#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:17:10 2017

@author: vittoriobisin
"""
from math import pi, sqrt, exp

def gauss(n,sigma):
    r = range(-int(n/2),int(n/2)+1)
    return [1 / (sigma * sqrt(2*pi)) * exp(-float(x)**2/(2*sigma**2)) for x in r]