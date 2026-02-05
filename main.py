from bot_logic import chatbot_response

print("🤖 AI Fitness Class Booking System")
user = input("Enter your name: ")

print(f"\nWelcome {user}! Type 'show classes' to begin. Type 'exit' to quit.\n")

while True:
    text = input("You: ")
    if text.lower() in ["exit", "quit", "bye"]:
        print("Bot: Bye! Stay fit 💪")
        break

    reply = chatbot_response(user, text)
    print("Bot:", reply)
