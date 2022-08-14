# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:20:43 2022

@author: HFernandezGarcia
"""



import matplotlib.pyplot as plt
import math
from numpy.linalg import norm
import numpy as np
from scipy import signal

import pixstem.api as ps

import utils
import plotting







def getpeaks_pixstem(dataarray):
    ps_obj = ps.PixelatedSTEM(dataarray)
    template = ps_obj.template_match_disk(disk_r=20, show_progressbar=True)
    peak_array = template.find_peaks(show_progressbar=True)
    pks = peak_array.compute().reshape(1)[0]
    return pks



def getpeaks(dataarray, s=8, refining=True):
    alpha=1.4
    p0ratio=0.01
    bgratio=1.5
    BGfrac=.25
    dim = len(dataarray)
    
    kern, kerf = createmasks(s)
    An, Af = np.sum(kern), np.sum(kerf)
    kern, kerf = kern/An, kerf/(Af/alpha)
    
    mapn = signal.correlate2d(dataarray, kern, "valid")
    mapf = signal.correlate2d(dataarray, kerf, "valid")
    
    BG = np.max(np.sort(dataarray.reshape(dim**2))[:round(BGfrac* dim**2)])
    MAX = np.max(mapn)
    TH = max(0*BG, p0ratio*MAX)
    
    pks=[]
    for x in range(dim-2*s):
        for y in range(dim-2*s):
            if mapn[y,x] > max(mapf[y,x], TH):
                pks.append([x+s, y+s])
    if refining:
        return refine(np.array(pks), 2*s, dim, s)
    return np.array(pks)


def createmasks(s):
    kern = np.zeros((2*s+1,2*s+1))
    kerf = np.zeros((2*s+1,2*s+1))
    for dx in range(-s, s+1):
        for dy in range(-s, s+1):
            kern[s+dx,s+dy] = int(math.sqrt(dx**2+dy**2) < s/2)
            kerf[s+dx,s+dy] = int(s/2 <= math.sqrt(dx**2+dy**2) <= s)
    return (kern, kerf)


def refine(peaks, radius, dim, offset=0):
    d = 3
    centers = []
    remaining = list(peaks)
    while(len(remaining)>0):
        new = remaining[:1]
        remaining = remaining[1:]
        box = np.array(2*new).transpose()
        while(True):
            toadd = []
            i=0
            newremaining = []
            while(i<len(remaining)):
                p = remaining[i]
                if( box[0,0]-d < p[0] < box[0,1]+d and box[1,0]-d < p[1] < box[1,1]+d and min( norm(p-p0) for p0 in new ) < d ):
                    toadd.append(p)
                else:
                    newremaining.append(p)
                i+=1
            if(len(toadd)==0):
                if(np.min(new)>offset+1 and np.max(new)<dim-offset):
                    centers.append(np.mean(new, axis=0))
                break
            else:
                remaining = newremaining[:]
                new += toadd
                xvals, yvals = list(np.array(toadd).transpose())
                box = np.array([ [min(np.min(xvals), box[0,0]), max(np.max(xvals), box[0,1])], [min(np.min(yvals), box[1,0]), max(np.max(yvals), box[1,1])] ])
    return np.array(centers)


def show_ED(shot, s=8, refining=True):
    dim = len(shot)
    ED_peaks = getpeaks(shot, s, refining=refining)
    num_ED_peaks = len(ED_peaks)
    pure = utils.from_peaks(ED_peaks, 1)
    
    plotting.ArrayPlot(shot)
    x, y = ED_peaks.transpose()
    plt.plot(x, y, 'ro', marker="o", markersize=2, markeredgecolor="red", markerfacecolor="green")
  
    
  
    
  
    
