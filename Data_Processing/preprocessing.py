#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:47:24 2022

@author: HemSem
"""
# import the libraries

import mne
# plt.close("all")

# import the data sets
def import_data(sample_data_raw_file):
    # sample_data_folder = mne.datasets.sample.data_path()
    # sample_data_raw_file = (sample_data_folder / 'MEG' / 'sample' /
    #                    'sample_audvis_filt-0-40_raw.fif')
    raw = mne.io.read_raw_edf(sample_data_raw_file) # reads in raw edf file
    print("raw data retrieved ")
    mne.viz.plot_raw(raw)
    print(raw.info)

    return raw

    # sample_data_folder = mne.datasets.sample.data_path()
    # sample_data_raw_file = (sample_data_folder / 'MEG' / 'sample' /
    #                         'sample_audvis_filt-0-40_raw.fif')
    # raw = mne.io.read_raw_fif(sample_data_raw_file)
    # return raw


def preprocessing_filter(raw):
    # here, we will filter the data between highpass = 0.1 Hz and lowpass = 40Hz
    # print('HERE ARE THE EVENTS')
    # events_from_annot, event_dict = mne.events_from_annotations(raw)
    # print(event_dict)
    # print(events_from_annot[:5])

    # ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
    # ica.fit(raw)
    # ica.exclude = [1, 2]  # exclude some of the traces
    # ica.plot_properties(raw, picks=ica.exclude)
    
    filtered_dataset = mne.filter.filter_data(raw, sfreq, l_freq, h_freq, picks=None, filter_length='auto', l_trans_bandwidth='auto', h_trans_bandwidth='auto', n_jobs=None, method='fir', iir_params=None, copy=True, phase='zero', fir_window='hamming', fir_design='firwin', pad='reflect_limited', *, verbose=None)[source]
    filtered_dataset = 1
    print('Filtering channels')
    return filtered_dataset
    #return filtered_datasets


def preprocessing_remove_channel(filtered_datasets):
    # here, we will get rid of the bad channels
    # this includes channels that have
    # (1) discontinuities
    # (2) channels that do not have data
    # (3) disconnected channels
    # (4) erroneous or noisy data
    # more to come about how this will be determined/automated
    picks = mne.pick_types(raw.info, meg=True, exclude='bads') 
    print("preprocessing channel remove execute")


    # ica.exclude = [1, 2]  # exclude some of the traces
    # ica.plot_properties(raw, picks=ica.exclude)

    print('Removing channels')
    pass
    #return remaining_channels
