from preprocessing import *
import numpy as np
import mne
import matplotlib.pyplot as plt
import pandas as pd

raw = import_data()
filter = preprocessing_filter(raw)
removed = preprocessing_remove_channel(filter)
removed = windowed_var(52, removed)
#removed.to_csv('test1.csv')
print(removed)
