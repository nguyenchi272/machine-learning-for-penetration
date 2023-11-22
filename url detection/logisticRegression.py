import numpy as np
from sklearn import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

training_data = np.genfromtxt(
    'Python/project/url detection/Training_Dataset.csv', delimiter=',', dtype=np.int32)

# inputs are all of attributes except the last one, outputs is the last attribute
inputs = training_data[:, :-1]
outputs = training_data[:, -1]

# divide the dataset into training data and testing data
training_inputs = inputs[:2000]
training_outputs = outputs[:2000]
testing_inputs = inputs[2000:]
testing_outputs = outputs[2000:]

# create a Logistic Regression classifier
clf = LogisticRegression()
clf.fit(training_inputs, training_outputs)

# Dự đoán và đánh giá mô hình
y_pred = clf.predict(testing_inputs)
accuracy = accuracy_score(testing_outputs, y_pred)
conf_matrix = confusion_matrix(testing_outputs, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
