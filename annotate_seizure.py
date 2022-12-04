#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:16:01 2022

@author: HemSem
"""


from Feature_Extraction import run_features
from Data_Processing import *
from ML_Model import *
import mne


filename = "/Users/HemSem/Documents/GitHub/ML-Seizure-Detection/dataset/s004_2016_09_26/00000086_s004_t003.edf"


raw = [] # Placeholder
# first import the raw edf data and plot visualization

raw = mne.io.read_raw_edf(filename) # reads in raw edf file
print("raw data retrieved ")
mne.viz.plot_raw(raw)
print(raw.info)




