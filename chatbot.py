print("AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")
    
    elif user == "how are you":
        print("Bot: I'm doing great!")
    
    elif user == "what is ai":
        print("Bot: AI means Artificial Intelligence.")
    
    elif user == "what is machine learning":
        print("Bot: Machine learning allows computers to learn from data.")
    
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    
    else:
        print("Bot: Sorry, I don't understand that yet.")
