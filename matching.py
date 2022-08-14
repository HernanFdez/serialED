# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:29:16 2022

@author: HFernandezGarcia
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm


import utils




def facetsimil(facet, base, hq): 
    q = np.dot(hq, base)
    p0, p1, Alpha = facet
    q0, q1, Beta = norm(q[0]), norm(q[1]), utils.VectorAngle(q[0], q[1])
    if( not(np.pi*(0) <= Beta <= np.pi*(2))):
        return(np.Infinity)
    hq0, hq1 = norm(hq[0]), norm(hq[1])
    Theta = np.arctan( np.tan(Alpha-Beta)/ (((p0*q0)/(p1*q1))*(hq0/hq1)**2 *1/np.cos(Alpha-Beta) +1));
    r = (p0**2 + q0**2 - 2*p0*q0*np.cos(Theta))*(hq0**2) + (p1**2 + q1**2 - 2*p1*q1*np.cos(Theta-(Alpha-Beta)))*(hq1**2);
    return(r)


def bestmatchcost(facet, base):
    M = 2
    costs = []
    idxs = []
    for h1 in range(-M,M+1):
        for k1 in range(-M,M+1):
            for l1 in range(-M,M+1):          
                if(np.gcd.reduce([h1, k1, l1]) == 1):
                    for h2 in range(-M,M+1):
                        for k2 in range(-M,M+1):
                            for l2 in range(-M,M+1):
                                if(np.gcd.reduce([h2, k2, l2]) == 1):
                                    hq = [[h1, k1, l1], [h2, k2, l2]];
                                    costs.append(facetsimil(facet, base, hq))
                                    idxs.append(hq)
    minPos = np.argmin(np.array(costs))            
    return (costs[minPos], idxs[minPos])
 

def fitcubic(facets, Set, a_range): 
    amin, amax, da = a_range
    calibration = 0.00847 # calibration factor (rec A per pixel), accounting for HV, camera length and pixel size, to go from pixels to A^-1
    units = np.array([[1,0,0],[0,1,0],[0,0,1]])
    costs=[]
    besthqs=[]
    a_vals = np.arange(amin, amax, da)
    for a in a_vals:
        base = (1/a)*units/calibration;
        a_costs = []
        a_besthqs = []
        for facet in facets:
            bestcost, besthq = bestmatchcost(facet, base)
            a_costs.append(bestcost/(2*len(facets)))
            a_besthqs.append(besthq)
        costs.append(a_costs)
        besthqs.append(a_besthqs)
        
    patterns_costs = np.array(costs).transpose()   
    totals = np.sqrt(np.sum(patterns_costs, axis=0))
    np.savetxt(Set+"_avals.txt", np.array([a_vals]))
    np.savetxt(Set+"_costs.txt", patterns_costs)
    plt.plot(a_vals, totals)
    plt.ylim([0,10])
    
    minPos = np.argmin(totals)
    bestfit = a_vals[minPos]
    bestfithqs = besthqs[minPos]
    return (bestfit, bestfithqs)



