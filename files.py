# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:16:18 2022

@author: HFernandezGarcia
"""


import os
import glob
import numpy as np

import hyperspy.api as hs



def gettilt(path, tilt='', lazy=True):
    if tilt!='':
        tilt = '_'+str(tilt)
    file = path + tilt + '.hspy'
    sig = hs.load(os.path.join(file), lazy=lazy)
    return sig


def getSerialData(Set):
    direct = os.path.dirname(Set)
    base = os.path.basename(Set).split(".")[0]
    os.chdir(direct)
    files = glob.glob(base+"_ED_*.txt")
    print(files)
    shots = []
    for file in files:
        shots.append(np.loadtxt(file))
    return shots