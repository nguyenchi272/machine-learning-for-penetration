import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Đọc dữ liệu từ file CSV
malware_data = pd.read_csv(
    'Python/project/PE detection/MalwareData.csv', sep='|')

# Loại bỏ các cột không cần thiết và lấy dữ liệu đặc trưng và nhãn
X = malware_data.drop(['Name', 'md5', 'legitimate'], axis=1).values
y = malware_data['legitimate'].values

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình Decision Tree
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Dự đoán và đánh giá mô hình
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
