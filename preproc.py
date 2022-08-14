# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:19:44 2022

@author: HFernandezGarcia
"""



import numpy as np
import pixstem.api as ps




def backgroundsub(dataarray):
    ps_signal = ps.PixelatedSTEM(dataarray)
    s_r = ps_signal.subtract_diffraction_background(method='median kernel', footprint=20, lazy_result=False, show_progressbar=True)
    arr = s_r.data
    arr /= np.max(arr)
    return arr