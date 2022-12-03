"""
More complicated features that perform transformations on signal
"""

import pandas as pd
import numpy as np
import pywt

def feature2A(signal: pd.DataFrame):
    """
    FeatureA (Example): Fourier transform into frequency domain

    Input: Post-processed signal in Pandas DataFrame format
        Other constants dependent on the feature

    Output: Feature in either numpy array or Pandas DataFrame
    """
    print("feature2a retrieved")

    return []

def feature2B(signal: pd.DataFrame):
    """
    FeatureB (Example): Discrete wavelet transform

    Input: Post-processed signal in Pandas DataFrame format
        Other constants dependent on the feature

    Output: Feature in either numpy array or Pandas DataFrame
    """
    
    cA = signal.copy()
    cD = signal.copy()

    cA.iloc[:,1:] = np.nan
    cD.iloc[:,1:] = np.nan

    cols = signal.columns[1:]
    for col in cols:
        (ca, cd) = pywt.dwt(signal[col], 'db1')
        cA.loc[1::2, col] = ca
        cD.loc[1::2, col] = cd

    return [cA, cD]

def feature2X(signal: pd.DataFrame):
    """
    Continue adding features that correlate with pre-seizure indication
    """
    print("Feature2x retrieved")
    return []
