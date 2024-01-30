def simple_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I help you today?"

    elif "how are you" in user_input.lower():
        return "I'm just a computer program, but thanks for asking!"

    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Example usage:
user_query = input("You: ")
response = simple_chatbot(user_query)
print("Chatbot:", response)