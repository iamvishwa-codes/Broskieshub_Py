def chatbot():
    print("Hello! I am your chatbot. Type 'bye' to exit.\n")

    # Lists of inputs
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    how_are_you = ["how are you", "how are you doing", "what's up"]
    name_queries = ["your name", "who are you", "what is your name"]
    weather_queries = ["weather", "temperature", "climate"]

    while True:
        user_input = input("You: ").lower()

        if user_input in greetings:
            print("Bot: Hi there! How can I help you?")

        elif user_input in how_are_you:
            print("Bot: I'm just a program, but I'm doing fine. How about you?")

        elif user_input in name_queries:
            print("Bot: I am a simple chatbot created with Python.")

        elif user_input in weather_queries:
            print("Bot: I can't check live weather yet, but it's always sunny in Python-land ☀️")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that. Try asking something else.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
