# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:40:38 2022

@author: HFernandezGarcia
"""


import math
import numpy as np



import utils
import plotting




def show_failures(roi_size, failures):
    fail_map = np.zeros((roi_size,)*2)
    for i in failures:
        fail_map[i//roi_size, i%roi_size] = 1
    plotting.ArrayPlot(fail_map, cmap='gray')
    
    
    
def show_orientation(angles, failures):
    angles = list(map(utils.reduce_hex, angles))
    num_patterns = len(angles) + len(failures)
    size = math.isqrt(num_patterns)
    if not (size**2 == num_patterns):
        print("not a square ROI")
        return
    
    for f in failures:
        angles = np.insert(angles, f, np.inf)
    angles = angles.reshape((size,)*2)    
    angles = np.ma.masked_where(angles == np.inf, angles)
    angles = angles.transpose()
    plotting.ArrayPlot(angles, colors='hsv')
    
    
    
    
    
    
    