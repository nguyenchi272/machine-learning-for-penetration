import os
import random
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer

# Đường dẫn đến thư mục chứa email spam và non-spam
spam_folder = 'Python/project/spam detection/spam_filter/enron1/spam'
ham_folder = 'Python/project/spam detection/spam_filter/enron1/ham'

# Hàm để đọc dữ liệu từ các tệp tin trong thư mục và gán nhãn


def read_files_from_folder(folder, label):
    emails = []
    files = os.listdir(folder)
    for file in files:
        with open(os.path.join(folder, file), 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            emails.append((content, label))
    return emails


# Đọc dữ liệu từ các tệp tin trong thư mục spam và gán nhãn là "spam"
spam_emails = read_files_from_folder(spam_folder, 'spam')

# Đọc dữ liệu từ các tệp tin trong thư mục non-spam và gán nhãn là "non-spam"
non_spam_emails = read_files_from_folder(ham_folder, 'non-spam')

# Kết hợp tập dữ liệu spam và non-spam
emails = spam_emails + non_spam_emails
random.shuffle(emails)

# Tạo danh sách các văn bản và nhãn tương ứng
texts = [email[0] for email in emails]
labels = [email[1] for email in emails]

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42)

# Xây dựng pipeline vector hóa dữ liệu văn bản và mô hình SVM
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Huấn luyện mô hình SVM
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_vectorized, y_train)

# Đánh giá mô hình
accuracy = svm_classifier.score(X_test_vectorized, y_test)
print("Accuracy:", accuracy)

# Sử dụng mô hình để dự đoán
example_email = "Congratulations! You've won a prize. Claim it now!"
example_email_vectorized = vectorizer.transform([example_email])
predicted_label = svm_classifier.predict(example_email_vectorized)
print("Predicted Label:", predicted_label)
