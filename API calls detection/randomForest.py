import csv
import random
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import scale

# Đọc và tiền xử lý dữ liệu
PRatio = 0.7
Dataset = open('Python/project/API calls detection/Android_Feats.csv')
Reader = csv.reader(Dataset)
Data = list(Reader)
Data = random.sample(Data, len(Data))
Data = np.array(Data)
Dataset.close()

cols = np.shape(Data)[1]
Y = Data[:, cols-1]
Y = np.array(Y)
Y = np.ravel(Y, order='C')
X = Data[:, :cols-1]
X = X.astype(np.float64)
X = scale(X)

# Chia tập dữ liệu thành tập huấn luyện và tập kiểm thử
PRows = int(PRatio * len(Data))
TrainD, TestD, TrainL, TestL = train_test_split(
    X, Y, test_size=0.3, random_state=42)

# Xây dựng mô hình Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(TrainD, TrainL)

# Dự đoán và đánh giá mô hình
Predictions = clf.predict(TestD)
Accuracy = metrics.accuracy_score(TestL, Predictions)
print(f'Accuracy: {Accuracy * 100:.2f}%')

# In đánh giá chi tiết
print('\nClassification Report:')
print(metrics.classification_report(TestL, Predictions))

# In ma trận nhầm lẫn
print('\nConfusion Matrix:')
print(metrics.confusion_matrix(TestL, Predictions))
