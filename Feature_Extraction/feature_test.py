from featureGroup1 import *
from featureGroup2 import *
from runFeatureMetrics import *
import pandas as pd

signal = pd.DataFrame()
error = 0
all_features = []

all_features.append(feature1A(signal))
all_features.append(feature1B(signal))
all_features.append(feature1X(signal))
all_features.append(feature2A(signal))
all_features.append(feature2B(signal))
all_features.append(feature2X(signal))
x = range(all_features.size())
for n in x:
    #if(all_features[n] != correct):
        #error += 1
        #print("error at feature %d", n)
        test_run = run_features(all_features)
#if test_run == incorrect:
    #error += 1
    #print(error running features)
print(error)
