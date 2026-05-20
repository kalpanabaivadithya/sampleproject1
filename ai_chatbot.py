print("🤖 Chatbot Started")
print("Type 'exit' to stop chatting\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Chatbot: Goodbye!")
        break

    elif user == "heloo" or user == "hello" or user == "hi":
        print("Chatbot: Hii! How can I help you?")

    elif "how are you" in user:
        print("Chatbot: I am fine. How about you?")

    elif "your name" in user:
        print("Chatbot: I am a Python Chatbot.")

    elif "python" in user:
        print("Chatbot: Python is a programming language.")

    elif "bye" in user:
        print("Chatbot: Bye! Have a nice day.")

    else:
        print("Chatbot: Sorry, I didn't understand that.")