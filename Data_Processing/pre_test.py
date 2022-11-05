from .preprocessing import *
import numpy as np
import mne
import matplotlib.pyplot as plt

#test import:
raw_test = import_data()
#tests for if raw data was properly imported
filter_test = preprocessing_filter(raw_test)
#tests for if data was properly filtered
removed_test = preprocessing_remove_channel(removed_test)
#tests for if channels were removed 
