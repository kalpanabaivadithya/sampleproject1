# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample dataset (replace with CSV if needed)
data = {
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham'],
    'message': [
        'Free entry in 2 a weekly competition',
        'Hey are we meeting today?',
        'Win cash prizes now!!!',
        'Call me when you are free',
        'Urgent! You have won a 1 week FREE membership',
        'Let us go for lunch',
        'Congratulations claim your reward',
        'Are you at home?'
    ]
}

df = pd.DataFrame(data)

# Convert labels to numbers
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['message']
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# -------------------------------
# Model 1: SVM Pipeline
# -------------------------------
svm_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', SVC(kernel='linear'))
])

svm_pipeline.fit(X_train, y_train)
svm_pred = svm_pipeline.predict(X_test)

print("SVM Accuracy:", accuracy_score(y_test, svm_pred))

# -------------------------------
# Model 2: Random Forest Pipeline
# -------------------------------
rf_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', RandomForestClassifier(n_estimators=100))
])

rf_pipeline.fit(X_train, y_train)
rf_pred = rf_pipeline.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))

# -------------------------------
# Test with custom message
# -------------------------------
test_msg = ["You won a free vacation!!! Click now"]

svm_result = svm_pipeline.predict(test_msg)
rf_result = rf_pipeline.predict(test_msg)

print("\nTest Message:", test_msg[0])
print("SVM Prediction:", "Spam" if svm_result[0] == 1 else "Not Spam")
print("Random Forest Prediction:", "Spam" if rf_result[0] == 1 else "Not Spam")# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample dataset (replace with CSV if needed)
data = {
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham'],
    'message': [
        'Free entry in 2 a weekly competition',
        'Hey are we meeting today?',
        'Win cash prizes now!!!',
        'Call me when you are free',
        'Urgent! You have won a 1 week FREE membership',
        'Let us go for lunch',
        'Congratulations claim your reward',
        'Are you at home?'
    ]
}

df = pd.DataFrame(data)

# Convert labels to numbers
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['message']
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# -------------------------------
# Model 1: SVM Pipeline
# -------------------------------
svm_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', SVC(kernel='linear'))
])

svm_pipeline.fit(X_train, y_train)
svm_pred = svm_pipeline.predict(X_test)

print("SVM Accuracy:", accuracy_score(y_test, svm_pred))

# -------------------------------
# Model 2: Random Forest Pipeline
# -------------------------------
rf_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', RandomForestClassifier(n_estimators=100))
])

rf_pipeline.fit(X_train, y_train)
rf_pred = rf_pipeline.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))

# -------------------------------
# Test with custom message
# -------------------------------
test_msg = ["You won a free vacation!!! Click now"]

svm_result = svm_pipeline.predict(test_msg)
rf_result = rf_pipeline.predict(test_msg)

print("\nTest Message:", test_msg[0])
print("SVM Prediction:", "Spam" if svm_result[0] == 1 else "Not Spam")
print("Random Forest Prediction:", "Spam" if rf_result[0] == 1 else "Not Spam")