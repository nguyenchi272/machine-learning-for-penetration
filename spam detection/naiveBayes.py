import os
import random
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
from collections import Counter
from nltk import NaiveBayesClassifier, classify

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

# Đọc dữ liệu từ các tệp tin trong thư mục ham và gán nhãn là "non-spam"
non_spam_emails = read_files_from_folder(ham_folder, 'non-spam')

# Kết hợp tập dữ liệu spam và non-spam
emails = spam_emails + non_spam_emails

# Hàm xử lý dữ liệu: loại bỏ dấu câu, chuyển về chữ thường, lemmatize và loại bỏ từ dừng


def process_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower())
              for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stop_words]
    return dict(Counter(tokens))


# Chuẩn bị dữ liệu huấn luyện
processed_emails = [(process_text(email), label) for (email, label) in emails]
random.shuffle(processed_emails)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
train_size = int(0.8 * len(processed_emails))
train_set = processed_emails[:train_size]
test_set = processed_emails[train_size:]

# Huấn luyện mô hình
classifier = NaiveBayesClassifier.train(train_set)

# Đánh giá mô hình
accuracy = classify.accuracy(classifier, test_set)
print("Accuracy testing is: ", classify.accuracy(classifier, test_set))

# Sử dụng mô hình để dự đoán
example_email = "Congratulations! You've won a prize. Claim it now!"
processed_email = process_text(example_email)
prediction = classifier.classify(processed_email)
print("Prediction for example email:", prediction)
