# -*- coding: utf-8 -*-
"""Phishing Email Detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17eFGYW8QmI8AXUkfVEyOAkq9evxofLrE
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = pd.read_csv("/content/Phishing_Email.csv")

# Feature Extraction (TF-IDF Vectorization)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
X = tfidf_vectorizer.fit_transform(data['EmailText'])
y = data['EmailType']  # '1' for phishing, '0' for legitimate

# Model Development (Random Forest Classifier)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluation (Accuracy)
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

from sklearn.metrics import confusion_matrix, classification_report

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Classification report
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)