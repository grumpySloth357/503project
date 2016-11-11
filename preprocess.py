import pandas as pd

#Import features
original_features = pd.read_csv('data_original/kddcup.names', delimiter=":", skiprows=1, header=None)
print original_features
