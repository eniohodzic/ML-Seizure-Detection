"""
This file will run all of the components

1) Data import
2) Data pre-processing and filtering 
3) Data formatting 
4) Feature extraction
5) Feature selection 
6) Model training and testing
"""

from Feature_Extraction import run_features
from Data_Processing import *
from ML_Model import *

def main():
# preprocessing
    # we will have a method to go through a patients dataset instead of just one file
    filename = "/Users/HemSem/Documents/GitHub/ML-Seizure-Detection/dataset/s003_2015_12_28/00000015_s003_t000.edf"
    
    # creates an empty variable for list data
    raw = [] # Placeholder
    # first import the raw edf data and plot visualization
    raw = import_data(filename)
    # filter the raw signal with preprocessing
    filtered_dataset = preprocessing_filter(raw)
    # remove bad channels from EEG data using MNE automated algorithms 
    signal = preprocessing_remove_channel(filtered_dataset)
    
    
    # ML portion
    features = run_features(signal) # processed, removed bad channels

    feats, labs = formatData(features, signal)
    splitData(feats, labs)

    models = chooseModel()
    checkModel()

    pass

if __name__ == '__main__':
    main()