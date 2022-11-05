#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:47:24 2022

@author: HemSem
"""
# import the libraries

import numpy as np
import mne
import matplotlib.pyplot as plt
# plt.close("all")

# import the data sets
def import_data():
    sample_data_folder = mne.datasets.sample.data_path()
    sample_data_raw_file = (sample_data_folder / 'MEG' / 'sample' /
                        'sample_audvis_filt-0-40_raw.fif')
                        raw = mne.io.read_raw_fif(sample_data_raw_file)
                        print("raw data retrieved")
return raw

    # sample_data_folder = mne.datasets.sample.data_path()
    # sample_data_raw_file = (sample_data_folder / 'MEG' / 'sample' /
    #                         'sample_audvis_filt-0-40_raw.fif')
    # raw = mne.io.read_raw_fif(sample_data_raw_file)

    print('Importing datasets')
    pass
    # return raw


def preprocessing_filter(raw):
    # here, we will filter the data between highpass = 0.1 Hz and lowpass = 40Hz


    # ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
    # ica.fit(raw)
    # ica.exclude = [1, 2]  # exclude some of the traces
    # ica.plot_properties(raw, picks=ica.exclude)

    print('Filtering channels')
    pass
    #return filtered_datasets


def preprocessing_remove_channel(filtered_datasets):
    # here, we will get rid of the bad channels
    # this includes channels that have
    # (1) discontinuities
    # (2) channels that do not have data
    # (3) disconnected channels
    # (4) erroneous or noisy data
    # more to come about how this will be determined/automated
    print("preprocessing channel remove execute")


    # ica.exclude = [1, 2]  # exclude some of the traces
    # ica.plot_properties(raw, picks=ica.exclude)

    print('Removing channels')
    pass
    #return remaining_channels
