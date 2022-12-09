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
To run visual features:
    -after downloading the directory run python3 __init__.py in ~\ML-Seizure-Detection\Data_Processing\
    -to visualize different types of windowed or fft features change the variable to_print in __init__.py to the desired value
    -the values of to_print correspond to:
        # 0 = fft of window 290-305 (figure 4) and 30-40 (figure 5)
        #1 = weighted averaged fft of 290-305
        #2 = 3 hz isolated of 290-305
        #3 = zerocrossings of 290-305
        #4 windowed average of 290-305
    =this will produce plots of the desired visual analysis tool as well as a printout of the raw data. 
