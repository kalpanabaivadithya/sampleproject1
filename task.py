import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

# ==============================
# DATABASE CONNECTION
# ==============================

conn = sqlite3.connect("chatbot.db", check_same_thread=False)
cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

# Create Chat History Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    username TEXT,
    question TEXT,
    answer TEXT
)
""")

conn.commit()

# ==============================
# FAQ DATA
# ==============================

faq_data = {
    "question": [
        "What courses are available?",
        "What is HR policy?",
        "How to reset password?",
        "What is product warranty?",
        "What are college timings?",
        "How to contact customer support?",
        "What is hostel fee?"
    ],

    "answer": [
        "We provide CSE, ECE, EEE and Mechanical courses.",
        "Employees get 20 leave days yearly.",
        "Click forgot password option.",
        "Warranty available for 1 year.",
        "College timings are 9 AM to 4 PM.",
        "You can contact support at support@gmail.com.",
        "Hostel fee is 50,000 per year."
    ]
}

data = pd.DataFrame(faq_data)

questions = data['question'].tolist()
answers = data['answer'].tolist()

# ==============================
# AI MODEL
# ==============================

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(questions)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

# ==============================
# CHATBOT FUNCTION
# ==============================

def get_answer(user_question):

    user_embedding = model.encode([user_question])

    D, I = index.search(np.array(user_embedding), k=1)

    return answers[I[0][0]]

# ==============================
# AUTHENTICATION FUNCTIONS
# ==============================

def register(username, password):

    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        (username, password)
    )

    conn.commit()

def login(username, password):

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    return cursor.fetchone()

# ==============================
# SAVE CHAT HISTORY
# ==============================

def save_chat(username, question, answer):

    cursor.execute(
        "INSERT INTO history VALUES (?, ?, ?)",
        (username, question, answer)
    )

    conn.commit()

# ==============================
# LOAD CHAT HISTORY
# ==============================

def get_history(username):

    cursor.execute(
        "SELECT question, answer FROM history WHERE username=?",
        (username,)
    )

    return cursor.fetchall()

# ==============================
# STREAMLIT UI
# ==============================

st.set_page_config(
    page_title="AI FAQ Chatbot",
    layout="wide"
)

st.title("🤖 AI FAQ Chatbot")

st.markdown("""
### Features
- College FAQs
- HR Support
- Customer Support
- Product Assistance
- Login/Register
- Chat History
- AI Search
""")

menu = ["Login", "Register"]

choice = st.sidebar.selectbox("Menu", menu)

# ==============================
# REGISTER PAGE
# ==============================

if choice == "Register":

    st.subheader("📝 Create New Account")

    new_user = st.text_input("Username")

    new_pass = st.text_input(
        "Password",
        type='password'
    )

    if st.button("Register"):

        register(new_user, new_pass)

        st.success("✅ Account Created Successfully")

# ==============================
# LOGIN PAGE
# ==============================

elif choice == "Login":

    st.subheader("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type='password'
    )

    if st.button("Login"):

        result = login(username, password)

        if result:

            st.success(f"✅ Welcome {username}")

            # ==============================
            # SIDEBAR HISTORY
            # ==============================

            st.sidebar.title("📜 Previous Chats")

            history = get_history(username)

            if history:

                for q, a in history:

                    st.sidebar.write("🧑", q)

            else:

                st.sidebar.write("No Previous Chats")

            # ==============================
            # CHAT SECTION
            # ==============================

            st.subheader("💬 Chat With AI")

            user_input = st.text_input(
                "Ask Any Question"
            )

            if st.button("Send"):

                response = get_answer(user_input)

                st.write("### 🤖 AI Response")

                st.success(response)

                # Save Chat
                save_chat(
                    username,
                    user_input,
                    response
                )

        else:

            st.error("❌ Invalid Username or Password")