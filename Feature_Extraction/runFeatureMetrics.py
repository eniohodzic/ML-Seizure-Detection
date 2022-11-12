"""
This functions serves as high level to run all feature functions and output a data type ready for model input
"""

import pandas as pd
from .featureGroup1 import *
from .featureGroup2 import *

def run_features(signal: pd.DataFrame, windowSize):
    """
    run_features: Runs all feature functions to return 

    Input: Post-processed signal in Pandas DataFrame format
        Other constants dependent on the features that are 

    Output: List of features to be input into machine learning model 
    """
    all_features = []

    all_features.append(calc_ROC(signal))
    all_features.append(calc_2nd_deriv(signal))
    all_features.append(local_STD(signal, windowSize))

    return all_features
