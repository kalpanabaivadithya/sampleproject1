import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

# File path
file_path = "spam.csv"

# Initialize vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Model
model = SGDClassifier(loss='log_loss')

# Label encoding
label_map = {'ham': 0, 'spam': 1}

chunk_size = 5000
first_chunk = True

for chunk in pd.read_csv(file_path, chunksize=chunk_size, encoding='latin1'):
    print("Processing new chunk...")

    # ✅ FIX: rename columns correctly
    chunk = chunk.rename(columns={'v1': 'label', 'v2': 'text'})

    # Convert labels
    chunk['label'] = chunk['label'].map(label_map)

    X = chunk['text']
    y = chunk['label']

    if first_chunk:
        X_vec = vectorizer.fit_transform(X)
        model.partial_fit(X_vec, y, classes=np.array([0, 1]))
        first_chunk = False
    else:
        X_vec = vectorizer.transform(X)
        model.partial_fit(X_vec, y)

print("\nTraining completed!")

# -------------------------
# Testing
# -------------------------

test_data = pd.read_csv(file_path, encoding='latin1').sample(1000)

# same fix again
test_data = test_data.rename(columns={'v1': 'label', 'v2': 'text'})

test_data['label'] = test_data['label'].map(label_map)

X_test = vectorizer.transform(test_data['text'])
y_test = test_data['label']

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# -------------------------
# Custom prediction
# -------------------------

msg = ["Congratulations! You won a free ticket"]
msg_vec = vectorizer.transform(msg)

prediction = model.predict(msg_vec)

if prediction[0] == 1:
    print("Spam Message")
else:
    print("Not Spam")