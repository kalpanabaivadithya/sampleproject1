import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# File path
file_path = "spam.csv"

# Initialize vectorizer (handles large data)
vectorizer = TfidfVectorizer(stop_words='english')

# Use partial fit model (good for large data)
model = SGDClassifier(loss='log_loss')  # logistic regression alternative

# Label encoding
label_map = {'ham': 0, 'spam': 1}

# Read large file in chunks
chunk_size = 5000
first_chunk = True

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    print("Processing new chunk...")

    # Convert labels
    chunk['label'] = chunk['label'].map(label_map)

    X = chunk['text']
    y = chunk['label']

    # Fit vectorizer only once
    if first_chunk:
        X_vec = vectorizer.fit_transform(X)
        model.partial_fit(X_vec, y, classes=np.array([0, 1]))
        first_chunk = False
    else:
        X_vec = vectorizer.transform(X)
        model.partial_fit(X_vec, y)

print("\nTraining completed!")

# -------------------------
# Testing the model
# -------------------------

# Load small test sample
test_data = pd.read_csv(file_path).sample(1000)

test_data['label'] = test_data['label'].map(label_map)

X_test = vectorizer.transform(test_data['text'])
y_test = test_data['label']

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# -------------------------
# Predict custom message
# -------------------------

msg = ["Congratulations! You won a free ticket"]
msg_vec = vectorizer.transform(msg)

prediction = model.predict(msg_vec)

if prediction[0] == 1:
    print("Spam Message")
else:
    print("Not Spam")