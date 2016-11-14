#Shreeya Khadka
#Convert all symbolic features into boolean vectors and save them onto file

import pandas as pd
import numpy as np

#Import features
original_features = pd.read_csv('data_shreeya/small.features.name', delimiter=":", skiprows=0, header=None)
num_features = len(original_features)
symbolic_features = original_features[0][original_features[1]==' symbolic.']
final_features = original_features[0][original_features[1]!=' symbolic.'].tolist()
Xtrain = pd.read_csv('data_shreeya/small.train.data', header=None)
Xoriginal = Xtrain.copy(deep=True)
#Split the labels Y from the X
Ytrain = Xtrain[num_features]
Xtrain.drop(num_features, axis=1, inplace=True)

features = original_features[0].tolist()
Xtrain.columns = features
Xoriginal.columns = features + ['label']
lenXtrain = len(Xtrain)

total_num_features = num_features - len(symbolic_features)
dfn_train = pd.DataFrame()
	
for sf in symbolic_features:
	options = Xtrain[sf].unique().tolist()
	stroptions = [sf+'_'+str(op) for op in options]
	#print sf,stroptions
	nfeat = len(options)
	total_num_features += nfeat
	
	ztrain = np.zeros((lenXtrain,nfeat))
	df_train = pd.DataFrame(ztrain,columns=stroptions)
	for i in range(nfeat):
		df_train[stroptions[i]][Xtrain[sf]==options[i]] = 1	
	#Remove the original column and replace with this new dataset
	final_features += stroptions
	#print final_features
	#print len(df)==lenXtrain
	Xtrain.drop(sf, axis=1, inplace=True)
	dfn_train = pd.concat([dfn_train,df_train], axis=1)
final_features = pd.DataFrame(final_features)
Xtrain = pd.concat([Xtrain,dfn_train], axis=1)

#Print results for verification!!!
#print 'Original festures:'
#print features
print '\n'
print 'Original Dataset:'
print Xoriginal
print '\n'
#print 'New Features:'
#print final_features
print 'New Dataset: <X>'
print (Xtrain)
print 'new Dataset: <Y>'
print Ytrain
