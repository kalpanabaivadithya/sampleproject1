import chatbot as st
from openai import OpenAI

# Set page title
st.set_page_config(page_title="Gen AI Chatbot")

st.title("🤖 Gen AI Chatbot")
st.write("Ask anything and get AI responses")

# Enter API key
api_key = st.text_input("Enter OpenAI API Key:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    # Store chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        # Get AI response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        bot_reply = response.choices[0].message.content

        # Save bot response
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

        with st.chat_message("assistant"):
            st.markdown(bot_reply)

else:
    st.warning("Please enter your OpenAI API key")