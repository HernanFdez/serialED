# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:34:18 2022

@author: HFernandezGarcia
"""

import time
import math
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt



import utils
import plotting
import files
import peaks
import facets
import matching


def show_AC_peaks(shot_raw, s=8):
    shot = shot_raw/np.max(shot_raw)
    dim = len(shot)
    ED_peaks = peaks.getpeaks(shot, s)
    num_ED_peaks = len(ED_peaks)
    pure = utils.from_peaks(ED_peaks, 1)
    
    plotting.ArrayPlot(shot)
    x, y = ED_peaks.transpose()
    plt.plot(x, y, 'ro', marker="o", markersize=2, markeredgecolor="red", markerfacecolor="green")
    plotting.ArrayPlot(pure)    
    
    autocorr = utils.autocorrelate(pure)/num_ED_peaks
    AC_peaks_raw = np.array((autocorr>1/4).nonzero()[::-1]).transpose()
    AC_peaks = peaks.refine(AC_peaks_raw, 2, dim, 4)
    
    plotting.ArrayPlot(autocorr)
    x, y = AC_peaks.transpose()
    plt.plot(x, y, 'ro', marker="o", markersize=2, markeredgecolor="red", markerfacecolor="green")
    
    center = np.array([dim/2, dim/2])
    head = dim*0.02
    base = facets.simplebase(AC_peaks)
    if len(base)<2:
        return
    
    print(base[0])
    print(base[1])
    print([norm(base[0]), norm(base[1]), utils.VectorAngle(base[0], base[1])])
    for v in base:
        plt.arrow(center[0], center[1], v[0], v[1], head_width=head, head_length=head, length_includes_head=True, color='black')
    
    plt.axline(center, slope=-base[0,0]/base[0,1], color="blue", linestyle=(5, (3, 6)))
    plt.axline(center + 0.51*base[0], slope=-base[0,0]/base[0,1], color="blue", linestyle=(5, (3, 6)))
  




def process_shots(shots, Set, s=8):
    failures = []
    peaks_all = []
    basis_all = []
    angles_all = []
    facets_all = []
    
    progress = 0.0
    num_shots = len(shots)
    t0 = time.time()
    for i in range(num_shots):
        shot = shots[i]
        ED_peaks = peaks.getpeaks(shot, s)
        if len(ED_peaks)<5:
            failures.append(i)
            continue
        pure = utils.from_peaks(ED_peaks, 1)
        
        autocorr = utils.autocorrelate(pure)/len(ED_peaks)        
        AC_peaks_raw = np.array((autocorr>1/4).nonzero()[::-1]).transpose()
        AC_peaks = peaks.refine(AC_peaks_raw, 2, len(shot), 4)

        basis = facets.simplebase(AC_peaks)
        if len(basis)<2:
            failures.append(i)
            continue
        angle = 0 if basis[0,0]==0 else np.arctan(basis[0,1]/basis[0,0])
        facet = facets.base2facet(basis)
        # print(i/num_shots, facet)
        current_progress = (1000*i//num_shots)/10
        if current_progress>progress:
            progress = current_progress
            print(str(progress) + ' % processed')
        
        peaks_all.append(AC_peaks.flatten())
        basis_all.append(basis.flatten())
        angles_all.append(angle)
        facets_all.append(facet)
    
    dt = time.time() - t0
    print('\nprocessed ' + str(num_shots) + ' patterns in ' + str(dt) + ' seconds: ' + str(dt/num_shots) + ' s/pattern')
    max_peaks = max([len(pks) for pks in peaks_all])
    peaks_all = [np.pad(pks, (0,max_peaks-len(pks))) for pks in peaks_all]
    
    np.savetxt(Set+ "_failures.txt", failures) 
    np.savetxt(Set+ "_peaks.txt", peaks_all) 
    np.savetxt(Set+ "_basis.txt", basis_all)
    np.savetxt(Set+ "_angle.txt", angles_all)
    np.savetxt(Set+ "_facet.txt", facets_all)
    
    
def rand_failure(Set):
    failures = np.loadtxt(Set+"_failures.txt", dtype=int)
    num_fails = len(failures)
    num_patterns = num_fails + len(np.loadtxt(Set+"_angle.txt"))
    
    size = math.isqrt(num_patterns)
    if not (size**2 == num_patterns):
        print("not a square ROI")
        return
    
    idx=failures[np.random.randint(num_fails)]
    x, y = idx//size, idx%size
    print("showing failure: ("+str(x)+","+str(y)+")")
    return (x, y)
    
    
    
def fit_set(Set, arange):
    print("fiting...")
    facets_all = np.loadtxt(Set+ "_facet.txt")
    bestfit, bestfithqs = matching.fitcubic(facets_all, Set, arange)
    uvws = [utils.normaluvw(np.cross(hkl[0], hkl[1])) for hkl in bestfithqs]
    np.savetxt(Set+ "_uvw.txt",np.array(uvws))
    np.savetxt(Set+ "_bestfit.txt",np.array([bestfit]))
    
    print(bestfit)
    for uvw in uvws:
        print(uvw)
        
    return bestfit



def fit_shots(shots, Set, arange, s=8):
    process_shots(shots, Set, s)
    fit_set(Set, arange)
    
    
def fitSerialData(Set, s=8):
    shots = files.getSerialData(Set)
    fit_shots(shots, Set, (3.0, 5.0, 0.1), s)

