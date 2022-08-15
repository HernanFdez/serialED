# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:14:52 2022

@author: HFernandezGarcia
"""


import copy
import matplotlib.pyplot as plt


import files


def ArrayPlot(data, colors='viridis'):
    cmap = copy.copy(plt.cm.get_cmap(colors))
    cmap.set_bad(color='black')
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(data, interpolation='nearest', cmap=cmap, vmin=0, vmax=1)
    fig.colorbar(cax)
    plt.show()
    
    
def Plot4D(path, tilt=''):
    files.gettilt(path, tilt, lazy=False).plot()
    
    
