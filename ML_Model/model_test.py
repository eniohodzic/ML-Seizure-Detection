from modelBuild import *
samp_feat, samp_sig = [],[]
samp_data = []
x,y = formatData(samp_feat, samp_sig)
X_train, X_test, y_train, y_test = splitData(x,y)
#tests for all variables above
test_model = chooseModel(samp_data)
#test for dictionary data type and vaid entries
checked = checkModel(samp_data, test_model)
#check for mdoel performance 
