"""
This functions serves as high level to run all feature functions and output a data type ready for model input
"""

import pandas as pd 
from featureGroup1 import *
from featureGroup2 import *

def run_features(signal: pd.DataFrame):
    
    all_features = []
    
    all_features.append(feature1A(signal))
    all_features.append(feature1B(signal))
    all_features.append(feature1X(signal))
    all_features.append(feature2A(signal))
    all_features.append(feature2B(signal))
    all_features.append(feature2X(signal))

    return all_features