# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:17:27 2022

@author: HFernandezGarcia
"""

import numpy as np


import files



def getshot(add, tilt, coors):
    x, y = coors
    sig = files.gettilt(add, tilt)
    pattern = sig.data[y,x]
    return pattern/np.max(pattern)

def take_shot(data, coors):
    x, y = coors
    pattern = data[y,x]
    return pattern/np.max(pattern)


def getshots(add, idx):
    shots = []
    for idx in idx:
        tilt, x, y = idx
        shots.append(getshot(add, tilt, [x,y]))
    return shots

def get_roi(data4D, size):
    shots = []
    for x in range(size):
        for y in range(size):
            shots.append(take_shot(data4D, [x,y]))
    return shots




