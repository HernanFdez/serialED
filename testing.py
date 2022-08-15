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



Set = r'D:\BigData\AutomatED_data\Graphene\Aperture_Overview_30kv_300pa_10WD_6kx\534x530'
# Set = r'D:\BigData\AutomatED_data\STO_np\Overview_30kv_100pa_10WD_4kx\138x66'
# Set = r'D:\BigData\AutomatED_data\Widefield\raw_dataset1'



sign = files.gettilt(Set)


# plotting.Plot4D(Set)
# plotting.ArrayPlot(datsets.take_shot(data, [7,7]))
# processing.show_AC_peaks(datasets.take_shot(sign, [455, 105]), s=4)


# shots = datasets.ROI(sign, 512)
# processing.process_shots(shots, Set, s=4)


# orientation.show_orientation(np.loadtxt(Set+"_angle.txt"), np.loadtxt(Set+"_failures.txt", dtype=int))
# plotting.ArrayPlot(datasets.take_shot(sign, processing.rand_failure(Set)))
# processing.show_AC_peaks(datasets.take_shot(sign, processing.rand_failure(Set)), s=4)


# shots = files.getSerialData(Set)
# processing.fitSerialData(Set)
# processing.fit_set(Set, (3.0, 5.0, 0.1))




