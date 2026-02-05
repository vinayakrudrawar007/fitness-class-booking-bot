# chatbot.py

import re

classes = {
    "yoga": 5,
    "zumba": 3,
    "hiit": 2
}

def show_classes():
    response = "Available classes:\n"
    for name, slots in classes.items():
        response += f"- {name.title()} (Slots: {slots})\n"
    return response

def book_class(user_input):
    for name in classes:
        if name in user_input:
            if classes[name] > 0:
                classes[name] -= 1
                return f"✅ Booking confirmed for {name.title()}! Remaining slots: {classes[name]}"
            else:
                return f"❌ Sorry, {name.title()} is fully booked."
    return "❗Please mention the class name (Yoga, Zumba, HIIT)."

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r"(hi|hello|hey)", user_input):
        return "Hey! 👋 I can help you book fitness classes. Type 'show classes' to see options."

    if "show" in user_input or "classes" in user_input:
        return show_classes()

    if "book" in user_input or "enroll" in user_input:
        return book_class(user_input)

    if "bye" in user_input or "exit" in user_input:
        return "Goodbye! 💪 Stay fit!"

    return "🤖 I didn't understand that. Try: 'show classes' or 'book yoga'."

if __name__ == "__main__":
    print("🤖 Fitness Class Booking AI Chatbot")
    print("Type 'show classes' or 'book yoga/zumba/hiit'. Type 'exit' to quit.\n")

   
