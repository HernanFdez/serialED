# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:24:44 2022

@author: HFernandezGarcia
"""


import numpy as np
from scipy import signal
from numpy.linalg import norm


def correlate2d(arr1, arr2, mode = 'valid'):
    return signal.fftconvolve(arr1, arr2[::-1, ::-1], mode = mode)


def autocorrelate(arr):
    return signal.fftconvolve(arr, arr[::-1, ::-1], mode='same')



def VectorAngle(v1, v2):
    return np.arccos(np.clip(np.dot(v1, v2)/(norm(v1)*norm(v2)), -1.0, 1.0))


def reduce_hex(ang):
    return (ang/(np.pi/3))%1


def normaluvw(uvw):
    fact = np.gcd.reduce(uvw)
    normalized = []
    for i in uvw:
        normalized.append(np.abs(i)/fact)
    return np.array(normalized)


def from_peaks(peaks, sigma):
    dim = 256
    s = 10*sigma
    ker = np.array([ [ np.exp(-(dx**2+dy**2)/(2*sigma**2))/(np.sqrt(np.pi)*sigma) for dy in range(-s, s+1)  ] for dx in range(-s, s+1) ])
    pure = np.zeros([dim]*2)
    
    for p in peaks:
        x0, y0 = np.round(p)
        x0, y0 = int(x0), int(y0)
        for dx in range(-min(s, x0), min(s, dim-x0)): 
            for dy in range(-min(s, y0), min(s, dim-y0)):
                pure[y0+dy, x0+dx] += ker[s+dy][s+dx]   
    return pure
 