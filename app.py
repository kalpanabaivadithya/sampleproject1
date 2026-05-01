import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# -------------------------------
# Load Dataset
# -------------------------------
data = pd.DataFrame({
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham'],
    'text': [
        'Win money now!!!',
        'Hello how are you',
        'Claim your prize now',
        "Let's meet tomorrow",
        'Free offer just for you',
        'Good morning'
    ]
})

# -------------------------------
# Train Model
# -------------------------------
X = data['text']
y = data['label']

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

# -------------------------------
# Prediction Function
# -------------------------------
def predict_message(message):
    msg_vec = vectorizer.transform([message])
    return model.predict(msg_vec)[0]

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("📩 Spam Detection App")

st.write("Enter a message to check whether it is Spam or Not Spam.")

user_input = st.text_area("Enter your message:")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        result = predict_message(user_input)

        if result == "spam":
            st.error("🚨 This is SPAM!")
        else:
            st.success("✅ This is NOT Spam")