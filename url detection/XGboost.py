import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Đọc dữ liệu từ file CSV
dataset = pd.read_csv(
    'Python/project/url detection/Training_Dataset.csv')

# Loại bỏ các cột không cần thiết và lấy dữ liệu đặc trưng và nhãn
X = dataset.drop(['Result'], axis=1).values
y = dataset['Result'].values

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42)
y_train = [0 if label == -1 else 1 for label in y_train]

# Xây dựng mô hình XGBoost
model = xgb.XGBClassifier(objective='binary:logistic', random_state=42)
model.fit(X_train, y_train)

# Đánh giá mô hình
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix:\n{conf_matrix}")
