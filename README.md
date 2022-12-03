# ML-Seizure-Detection

Directory Structure:
    Data_Processing serves to contain all functions related to data importation, formatting, filtering, and preprocessing before features are computed on the signal channels
    Feature_Extraction serves to contain all functions related to computing features that will be fed into the model, takes input from Data_Processing
    ML_Model contains all related functions to computing the ML model and evalutating the performance using features comptued from Feature_Extraction
    test contains test scripts on functions used throughout pipeline
Must hae Numba version 0.48.0, install pandas, mne, and numpy

How to run:
    Download the entire root directory using `git clone https://github.com/eniohodzic/ML-Seizure-Detection.git`
    run the following command `python main.py` while cd in location of download
    to test run each of the respective test modules:
    - `Data_Processing\pre_test.py`
    - `Feature_Extraction\feature_test/py`
    - `ML_Model\model_test.py`
