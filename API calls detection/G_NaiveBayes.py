
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score

data = pd.read_csv('Python/project/API calls detection/Android_Feats.csv')
# Tách dữ liệu thành tập dữ liệu và nhãn
cols = np.shape(data)[1]
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Tạo mô hình Gaussian Naive Bayes
gnb = GaussianNB()

# Huấn luyện mô hình trên tập huấn luyện
gnb.fit(X_train, y_train)

# Dự đoán nhãn trên tập kiểm tra
y_pred = gnb.predict(X_test)

# Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
