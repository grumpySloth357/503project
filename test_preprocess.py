#Shreeya Khadka
#Convert all symbolic features into boolean vectors and save them onto file

import pandas as pd
import numpy as np

#Import features
original_features = pd.read_csv('data_original/kddcup.names', delimiter=":", skiprows=1, header=None)
num_features = len(original_features)
symbolic_features = original_features[0][original_features[1]==' symbolic.']
final_features = original_features[0][original_features[1]!=' symbolic.'].tolist()
Xtrain = pd.read_csv('data_original/kddcup.data.gz', header=None)
Xtest = pd.read_csv('data_original/corrected.gz', header=None)
#Split the labels Y from the X
Ytrain = Xtrain[num_features]
Xtrain.drop(num_features, axis=1, inplace=True)
Ytest = Xtest[num_features]
Xtest.drop(num_features, axis=1, inplace=True)

features = original_features[0]
Xtrain.columns = features
Xtest.columns = features
lenXtrain = len(Xtrain)
lenXtest = len(Xtest)

total_num_features = num_features - len(symbolic_features)
dfn_train = pd.DataFrame()
dfn_test = pd.DataFrame()	
for sf in symbolic_features:
	options = Xtrain[sf].unique().tolist()
	stroptions = [sf+'_'+str(op) for op in options]
	#print sf,stroptions
	nfeat = len(options)
	total_num_features += nfeat
	
	ztrain = np.zeros((lenXtrain,nfeat))
	ztest = np.zeros((lenXtest,nfeat))
	df_train = pd.DataFrame(ztrain,columns=stroptions)
	df_test = pd.DataFrame(ztest,columns=stroptions)
	for i in range(nfeat):
		df_train[stroptions[i]][Xtrain[sf]==options[i]] = 1
		df_test[stroptions[i]][Xtest[sf]==options[i]] = 1
	#Remove the original column and replace with this new dataset
	final_features += stroptions
	#print final_features
	#print len(df)==lenXtrain
	Xtrain.drop(sf, axis=1, inplace=True)
	Xtest.drop(sf,axis=1, inplace=True)
	dfn_train = pd.concat([dfn_train,df_train], axis=1)
	dfn_test = pd.concat([dfn_test,df_test],axis=1)
final_features = pd.DataFrame(final_features)
final_features.to_csv('data_shreeya/features.name',header=False,index=False)
Xtrain = pd.concat([Xtrain,dfn_train], axis=1)
print Xtrain.columns
Xtrain.to_csv('data_shreeya/train.data.gz',compression='gzip',header=False,index=False)
Ytrain.to_csv('data_shreeya/train.label',header=False,index=False)
print Xtest.columns
Xtest = pd.concat([Xtest,dfn_test],axis=1)
Xtest.to_csv('data_shreeya/test.data.gz',compression='gzip',header=False,index=False)
Ytest.to_csv('data_shreeya/test.label',header=False,index=False)
