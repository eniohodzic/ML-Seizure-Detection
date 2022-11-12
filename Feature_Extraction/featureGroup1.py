"""
Simple features only on time domain of signal
"""

import pandas as pd
import numpy as np

def calc_ROC(signal: pd.DataFrame):
    """
    FeatureA (Example): first derivative ROC of EEG signal

    Input: Post-processed signal in Pandas DataFrame format
        Other constants dependent on the feature

    Output: Feature in either numpy array or Pandas DataFrame
    """

    ROC_df = signal.diff(periods=1, axis=0)
    ROC_df.iloc[:,1:] = ROC_df.iloc[:,1:].div(ROC_df.time, axis=0)
    ROC_df.time = signal.time

    return ROC_df

def calc_2nd_deriv(signal: np.array):
    """
    FeatureB (Example): second derivative of signal 

    Input: Post-processed signal in Pandas DataFrame format
        Other constants dependent on the feature

    Output: Feature in either numpy array or Pandas DataFrame
    """

    sec_deriv_df = signal.diff(periods=1, axis=0).diff(periods=1, axis=0)
    time_change = signal.diff(periods=1, axis=0).time
    sec_deriv_df.iloc[:,1:] = sec_deriv_df.iloc[:,1:].div(time_change, axis=0)
    sec_deriv_df.time = signal.time

    return sec_deriv_df

def local_STD(signal: np.array, window_size = 10):
    """
    Provide rolling window standard deviation
    """

    STD_df = signal.rolling(window_size).std()
    STD_df.time = signal.time

    return STD_df
