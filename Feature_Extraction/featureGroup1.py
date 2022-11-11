"""
Simple features only on time domain of signal
"""

import pandas as pd

def feature1A(signal: pd.DataFrame):
    """
    FeatureA (Example): first derivative ROC of EEG signal

    Input: Post-processed signal in Pandas DataFrame format
        Other constants dependent on the feature

    Output: Feature in either numpy array or Pandas DataFrame
    """
    print("feature1a retrieved")

    return []

def feature1B(signal: pd.DataFrame):
    """
    FeatureB (Example): local variance of EEG signal

    Input: Post-processed signal in Pandas DataFrame format
        Other constants dependent on the feature

    Output: Feature in either numpy array or Pandas DataFrame
    """
    print("feature1b retrieved")

    return []

def feature1X(signal: pd.DataFrame):
    """
    Continue adding features that correlate with pre-seizure indication
    """
    print("feature1x retrieved")
    return []
