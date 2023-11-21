from sklearn.feature_selection import mutual_info_classif
from sklearn import preprocessing
import numpy as np
from sklearn.svm import SVC, LinearSVC
from sklearn import svm
import csv
import random

# pre-process the CSV file
PRatio = 0.7
Dataset = open('Python/project/API calls detection/Android_Feats.csv')
Reader = csv.reader(Dataset)
Data = list(Reader)
Data = random.sample(Data, len(Data))
Data = np.array(Data)
Dataset.close()

# Identity the data and the labels
cols = np.shape(Data)[1]
Y = Data[:, cols-1]
Y = np.array(Y)
Y = np.ravel(Y, order='C')
X = Data[:, :cols-1]
X = X.astype(np.float64)
X = preprocessing.scale(X)

# extract the most important features
Features = [i.strip()
            for i in open("Python/project/API calls detection/Android_Feats.csv").readlines()]
Features = np.array(Features)
MI = mutual_info_classif(X, Y)
Featuresind = sorted(range(len(MI)), key=lambda i: MI[i], reverse=True)[:50]
SelectFeats = Features[Featuresind]

# divide dataset into training and testing sets
PRows = int(PRatio*len(Data))
TrainD = X[:PRows, Featuresind]
TrainL = Y[:PRows]
TestD = X[PRows:, Featuresind]
TestL = Y[PRows:]

# train the model
clf = svm.SVC()
clf.fit(TrainD, TrainL)
score = clf.score(TestD, TestL)
print(score*100)
