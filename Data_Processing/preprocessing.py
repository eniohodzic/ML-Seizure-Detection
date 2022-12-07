#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:47:24 2022

@author: HemSem
"""
# import the libraries

import mne
import numpy as np
import numba
import pandas as pd
from numpy.fft import fft, ifft
# plt.close("all")
#need version 1.20.0 of numpy and ver 0.48 of numba to run

# import the data sets
def import_data():
    #sample_data_folder = '~/Data_Processing'
    #sample_data_raw_file = (sample_data_folder / 'MEG' / 'sample' /
    #                    'sample_audvis_filt-0-40_raw.fif')
    raw = mne.io.read_raw_edf('00000124_s008_t028.edf', preload = True)
    print("raw data retrieved")
    return raw

    # sample_data_folder = mne.datasets.sample.data_path()
    # sample_data_raw_file = (sample_data_folder / 'MEG' / 'sample' /
    #                         'sample_audvis_filt-0-40_raw.fif')
    # raw = mne.io.read_raw_fif(sample_data_raw_file)
    # return raw


def preprocessing_filter(raw):
    # here, we will filter the data between highpass = 0.1 Hz and lowpass = 40Hz
    # ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
    # ica.fit(raw)
    # ica.exclude = [1, 2]  # exclude some of the traces
    # ica.plot_properties(raw, picks=ica.exclude)
    to_drop = []
    #for(i in range(x)):
        #scan through for bad channels under certain conditions TBD
        #to_drop.append(y)
    to_drop.append('EEG C3-REF') #test value
    #print(to_drop)
    raw.drop_channels(to_drop)
    raw.notch_filter(np.arange(60, 100, 60))
    raw.plot()
    return raw
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

    return filtered_datasets.to_data_frame()
    # ica.exclude = [1, 2]  # exclude some of the traces
    # ica.plot_properties(raw, picks=ica.exclude)
    #return remaining_channels
def windowed_var(window, df):
    vr = df.rolling(window).var()
    vr["time"] = df["time"]
    return vr


def window_remove_nan(df):
    return df.dropna()


def windowed_avg(window, df):
    absmean = lambda x: np.mean(abs(x))
    mn = df.rolling(window).apply(absmean)
    mn["time"] = df["time"]
    return

def zerocross(df):
    #assumtion" all zeros are crossing due to varaiablilty of noise
    zerocross = lambda x: ((abs(np.sum(x)) != np.sum(abs(x))))|(np.all(x)==False)
    zc = df.rolling(2).apply(zerocross)
    zc["time"] = df["time"]
    return zc

def windowed_fft_avg(window, df, weight_type = 0, weight = 2):
    scaler = np.arange(window) + 1
    if weight_type == 1:
        scaler = np.logspace(1,window,num = window, base = weight)
    fourier = lambda x: abs(np.mean(np.multiply(fft(x),scaler)))
    ft = df.rolling(52).apply(fourier)
    ft["time"] = df["time"]
    return ft


def window_fft_3hz_est(sampling_frq, df):
    window = 1//sampling_frq
    fourier = lambda x: abs((fft(x)[4]))
    ft = df.rolling(window).apply(fourier)
    ft["time"] = df["time"]
    return ft

def detect_freq(df):
    for i in np.arange(10):
        timescale += df["time"].iloc[i+1] - df["time"].iloc[i]
    return freq = 10//timescale
