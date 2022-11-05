from modelBuild import *
samp_feat, samp_sig = None, None
x,y = formatData(samp_feat, samp_sig)
X_train, X_test, y_train, y_test = splitData(x,y)
#tests for all variables above
