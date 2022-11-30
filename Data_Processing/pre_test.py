from preprocessing import *
import numpy as np
import mne
import matplotlib.pyplot as plt

#test import:
error = 0
raw_test = import_data()
#tests for if raw data was properly imported
#if (raw_test == false):
    #print(error code)
    #error +=1
filter_test = preprocessing_filter(raw_test)
#tests for if data was properly filtered
#if(filter_test == false):
    #print(error code)
    #error +=1
removed_test = preprocessing_remove_channel(filter_test)
#tests for if channels were removed
#if(removed_test == false):
    #print(error code)
    #error +=1
print(error)
