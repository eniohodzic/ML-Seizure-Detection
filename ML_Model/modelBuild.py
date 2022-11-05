import pandas as pd
import numpy as np
import mne
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split



def formatData(features, signal):

    """
    Format the features and signal data in such a way for proper model training

    Input: features and signal dataframe and/or list

    Output: a two-dimensional array with appropriate features and label(s)

    """

    feats = []
    labs = []

    print('Formating features')
    return feats, labs


def splitData(X, y):
    """
    Split the properly formatted data into training and testing with an 80-20 split

    Input: properly formatted dataframe of the features and signal data

    Output: arrays of training and testing data
    """

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    print('Splitting data')
    pass
    # return X_train, X_test, y_train, y_test


def chooseModel():
    """
    Try and build different models to fit the data to. Evaluate each model with cross-validation to determine which model is best suited for EEG detection

    Input: arrays of training data 

    Output: dictionary of model name as keys, and performance metrics as values
    
    """

    print('Returning all models')
    return {}


def checkModel():
    """
    Test the chosen model's performance from chooseModel() in the testing data

    Input: array of testing data, model from chooseModel with best performance

    Output: performance metrics on testing dataset, object model of choice

    """

    print('Selecting best model')
    return None
