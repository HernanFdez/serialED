# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:41:57 2022

@author: HFernandezGarcia
"""

import numpy as np



import files
import plotting
import datasets
import processing
import orientation



Set = r'D:\BigData\AutomatED_data\STO_4DSTEM_Data\ED_data\STO_nanoparticles_tomo'
# Set = r'D:\BigData\AutomatED_data\Saleh\STO_np\Overview_30kv_100pa_10WD_4kx\138x66'

# shot = files.getSerialData(Set)[1]
# processing.showautocorrpeaks(shot)



# data = files.gettilt(Set, 6).data

# plotting.Plot4D(Set, 6)

# shts = datasets.get_roi(data, 16)
# processing.process_shots(shts, Set, s=4)

# orientation.show_orientation(np.loadtxt(Set+"_angle.txt"), np.loadtxt(Set+"_failures.txt", dtype=int))


# processing.showautocorrpeaks(datasets.take_shot(data, processing.rand_failure(Set)), s=4)

# plotting.ArrayPlot(datsets.take_shot(data, [7,7]))

# processing.showautocorrpeaks(datasets.take_shot(data, [7, 5]), s=4)



# processing.fitSerialData(Set)

# processing.fit_set(Set, (3.0, 5.0, 0.1))

# sots = files.getSerialData(Set)
# processing.fitSerialData(Set)




