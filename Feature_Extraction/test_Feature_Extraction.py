from .featureGroup1 import *
from .featureGroup2 import *
from .runFeatureMetrics import *
import pandas as pd
import mne 
from os.path import dirname, join 

def import_sample():

    project_root = dirname(dirname(__file__))
    file = r'00000015_s003_t000.edf'
    path = join(project_root, 'dataset', 's003_2015_12_28', file)
    raw = mne.io.read_raw_edf(path)
    
    return pd.DataFrame(raw.to_data_frame())

def test_calc_ROC():
    raw = import_sample()
    df = calc_ROC(raw)
    assert(df.shape == raw.shape)
    assert(any(df))

def test_calc_2nd_deriv():
    raw = import_sample()
    df = calc_2nd_deriv(raw)
    assert(df.shape == raw.shape)
    assert(any(df))

def test_local_STD():
    raw = import_sample()
    df = local_STD(raw)
    assert(df.shape == raw.shape)
    assert(any(df))

