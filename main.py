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

    raw = [] # Placeholder
    import_data()
    filtered_dataset = preprocessing_filter(raw)
    signal = preprocessing_remove_channel(filtered_dataset)

    features = run_features(signal)

    feats, labs = formatData(features, signal)
    X_train, X_test, y_train, y_test = splitData(feats, labs)

    model = chooseModel(X_train, X_test, y_train, y_test)
    checkModel(X_train, X_test, y_train, y_test, model)

    pass

if __name__ == '__main__':
    main()