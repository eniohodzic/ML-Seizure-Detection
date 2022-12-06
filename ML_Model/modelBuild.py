import pandas as pd
import numpy as np
import mne
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def reformat(featureData):
    """
    Reformat the 3D data for one patient (time x channels x features) to a 2D time x channelFeatures

    Input: 3D data for one patient (time x channels x features)
    
    Output: 2D time x channelFeatures

    """

    return featureData.reshape(featureData.shape[0], -1)

def formatData(allFeatureData):

    """
    Format the features and signal data in such a way for proper model training

    Input: 4D features data with the fourth dimension being each patient

    Output: a two-dimensional array concatenated row-wise for each patient

    """
    patientCount = allFeatureData.shape[3]
    final = reformat(allFeatureData[:,:,:,0]) # initiate the array 
    for i in patientCount[1:]: # start from second patient because first patient has been run above
        tmp = reformat(allFeatureData[:,:,:,i]) # the conversion from 3D to 2D
        final.append(final, tmp, axis = 0) # stack (row-wise) for each patient

    feature = final[:,:-2]
    label = final[:,-1]
    print("signal formatted")
    return feature, label


def splitData(X, y):
    """
    Split the properly formatted data into training and testing with an 80-20 split

    Input: properly formatted dataframe of the features and signal data

    Output: arrays of training and testing data
    """

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    print("signal split")

    return X_train, X_test, y_train, y_test


def chooseModel(X_train, X_test, y_train, y_test):
    """
    Try and build different models to fit the data to. Evaluate each model with cross-validation to determine which model is best suited for EEG detection

    Input: arrays of training data

    Output: dictionary of model name as keys, and performance metrics as values

    """
    models = []
    models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
    # models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    # models.append(('CART', DecisionTreeClassifier()))
    # models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(gamma='auto')))

    results = []
    names = []
    for name, model in models:
        kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
        cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
        results.append(cv_results)
        names.append(name)
        print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))


    best_idx = np.argmax(results)
    best_model = names[best_idx]
    best_acc = results[best_idx]

    print(f"Model chosen is {best_model} with an accuracy of {best_acc}")

    return best_model


def checkModel(X_train, X_test, y_train, y_test, chosen_model):
    """
    Test the chosen model's performance from chooseModel() in the testing data

    Input: array of testing data, model from chooseModel with best performance

    Output: performance metrics on testing dataset, object model of choice

    """
    str_to_model = {'LR':LogisticRegression(solver='liblinear', multi_class='ovr'),
                    'KNN':KNeighborsClassifier(),
                    'SVM':SVC(gamma='auto')
                    }
    model = str_to_model[chosen_model]
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc_score = accuracy_score(y_test, predictions)

    print(f'Score on testing dataset: {acc_score}')
    print("Model checked")

    return None
