# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:26:31 2022

@author: HFernandezGarcia
"""



import numpy as np
from numpy.linalg import norm


import utils





def simplebase(peaks):
    if(len(peaks)<5):
        return []
    dim = 256
    centered = peaks-dim/2
    srtd = centered[(centered[:,0]**2+centered[:,1]**2).argsort()][1:]
    
    p0, rest = srtd[0], srtd[1:];    
    u0 = p0/norm(p0) 
    proj = np.array([ np.dot(u0, p1)/norm(p1) for p1 in rest])
    filtered = rest[(0 <= proj) * (proj < 0.7)];
    if len(filtered)==0:
        return []
    return np.array([p0, filtered[0]])


def base2facet(base):
    a, b = base
    facet = [norm(a), norm(b), utils.VectorAngle(a, b)]
    return np.array(facet)
    


def mainfacet(peaks):
    return base2facet(simplebase(peaks))




