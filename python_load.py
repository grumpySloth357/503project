#Use python to make sparse Xtrain,Xtest matrices and save it as .mat

from scipy import sparse, io, vstack
import pandas as pd

#load the huge ass file
Xtest = pd.read_csv('data_shreeya/test.data.gz',compression='gzip' ,header=None)
#print Xtest
#print "making sparse"
Xtest = sparse.coo_matrix(Xtest)
#print Xtest
#print "saving..."
#Save as .mat
io.savemat('data_shreeya/test.data.mat', {'Xtest':Xtest})
print 'test file done...'
#load the huge ass file
print 'loading TRAIN file...'
Xtrain = sparse.coo_matrix([])
for x in pd.read_csv('data_shreeya/train.data.gz',compression='gzip' ,header=None, chunksize=100000):
	print "making sparse"
	x = sparse.coo_matrix(x)
	Xtrain =sparse.vstack((Xtrain,x),format='coo')
print Xtrain
print "saving..."
#Save as .mat
io.savemat('data_shreeya/train.data.mat', {'Xtrain':Xtrain})

