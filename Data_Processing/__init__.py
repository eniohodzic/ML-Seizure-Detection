from preprocessing import *
import numpy as np
import mne
import matplotlib.pyplot as plt
import pandas as pd
from numpy.fft import fft

raw = import_data()
filter = preprocessing_filter(raw)
removed = preprocessing_remove_channel(filter)
print(removed)
start = 290*256
finish = 305*256
re = removed.iloc[start:finish]
print(re)






#plt.figure(6)
#three.plot(x = 'time', y= "EEG T1-REF")
#print(re)

#removed.to_csv('test1.csv')
#print(removed)

#change varaible to change printed plot
# 0 = fft of window 290-305 (figure 4) and 30-40 (figure 5)
#1 = weighted averaged fft of 290-305
#2 = 3 hz isolated of 290-3050
#3 = zerocrossings of 290-305
#4 windowed average of 290-305
to_print = 5
if to_print == 0:
    a = 300 * 256
    b = 305*256
    re1 = removed.iloc[a:b]
    to_fft1 = re1["EEG T1-REF"].to_numpy()
    fft_arb1 = fft(to_fft1)[0:128]
    freq1 = np.arange(len(fft_arb1))
    freq1 = freq1*(256/len(freq1))
    freq1 = freq1

    s2 = 290*256
    s3 = 295*256
    rev = removed.iloc[s2:s3]
    to_fft2 = rev["EEG T1-REF"].to_numpy()
    fft_arb2 = fft(to_fft2)[0:128]
    freq2 = np.arange(len(fft_arb2))
    freq2 = freq2*(256/len(freq2))
    freq2 = freq2
    plt.figure(4)
    plt.stem(freq1, np.abs(fft_arb1), 'b', markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.figure(5)
    plt.stem(freq2, np.abs(fft_arb2), 'b', markerfmt=" ", basefmt="-b")
    plt.ylim([0, 50000])
    plt.xlabel('Freq (Hz)')
elif to_print == 1:
    proc = windowed_fft_avg(256, re, weight_type = 1, weight = 1.5)
    plt.figure(6)
    proc.plot(x = 'time', y= "EEG T1-REF")
elif to_print == 2:
    plt.figure(6)
    three = window_fft_3hz_est(256, re)
    three.plot(x = 'time', y= "EEG T1-REF")
elif to_print == 3:
    plt.figure(6)
    zc = zerocross(re)
    zc.plot(x = 'time', y= "EEG T1-REF")
elif to_print == 4:
    plt.figure(6)
    wa = windowed_avg(52, re)
    wa.plot(x = 'time', y= "EEG T1-REF")
elif to_print == 5:
    plt.figure(6)
    vr = windowed_var(52, re)
    vr.plot(x = 'time', y= "EEG T1-REF")
plt.show()
