#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 10:03:24 2017

@author: vittoriobisin
"""

def TVNorm(x):
    import numpy as np
    return sum(abs(np.diff(x,axis=0)))