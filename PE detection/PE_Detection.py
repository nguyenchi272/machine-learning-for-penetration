import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import confusion_matrix

MalwareDataset = pd.read_csv('Downloads/MalwareData.csv', sep='|')
Legit = MalwareDataset[0:41323].drop(['legitimate'], axis=1)
malware = MalwareDataset[41323::].drop(['legitimate'], axis =1)

Data = MalwareDataset.drop(['Name', 'md5', 'legitimate'], axis=1).values #loai bo ten, md5 va trang thai 'legitimate' de tao du lieu
Target = MalwareDataset['legitimate'].values

#chon ra cac dac trung quan trong de huan luyen mo hinh
FeatSelect = sklearn.ensemble.ExtraTreesClassifier().fit(Data, Target)
Model = SelectFromModel(FeatSelect, prefit=True)
Data_new = Model.transform(Data)

#chia du lieu thanh cac tap huan luyen va kiem tra
Legit_Train, Legit_Test, Malware_Train, Malware_Test = model_selection.train_test_split(Data_new, Target, test_size=0.2)

#huan luyen mo hinh Random Forest voi 50 cay quyet dinh
clf = sklearn.ensemble.RandomForestClassifier(n_estimators=50)
clf.fit(Legit_Train, Malware_Train)
score = clf.score(Legit_Test, Malware_Test)
print("The score of Random Forest Algorithm is: ", score*100)

#danh gia hieu suat mo hinh bang FPR va FNR
Result = clf.predict(Legit_Test)
CM = confusion_matrix(Malware_Test, Result)
print('False positive rate: %f %%' % ((CM[0][1] / float(sum(CM[0]))) *100))
print('False negative rate: %f %%' % ((CM[1][0] / float(sum(CM[1])) *100)))