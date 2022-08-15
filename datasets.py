# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:17:27 2022

@author: HFernandezGarcia
"""

import numpy as np


import files


class ROI:
    def __init__(self, sign, size):
        self.sign = sign
        self.size = size
        
    def __getitem__(self, i):
        x, y = i//self.size, i%self.size
        return take_shot(self.sign, [x,y])
    
    def __len__(self):
        return self.size**2


def getshot(add, tilt, coors):
    x, y = coors
    sig = files.gettilt(add, tilt)
    pattern = sig.data[y,x]
    return pattern/np.max(pattern)

def take_shot(sign, coors):
    x, y = coors
    pattern = sign.data[y,x].compute()
    return pattern/np.max(pattern)


def getshots(add, idx):
    shots = []
    for idx in idx:
        tilt, x, y = idx
        shots.append(getshot(add, tilt, [x,y]))
    return shots

def get_roi(sign, size):
    shots = []
    for x in range(size):
        for y in range(size):
            shots.append(take_shot(sign, [x,y]))
    return shots




