import re
from data import classes, bookings

def show_classes():
    msg = "📋 Available Fitness Classes:\n"
    for name, info in classes.items():
        msg += f"- {name.title()} at {info['time']} | Slots: {info['slots']}\n"
    return msg

def book_class(user, text):
    for name in classes:
        if name in text:
            if classes[name]["slots"] > 0:
                classes[name]["slots"] -= 1
                bookings.append({"user": user, "class": name})
                return f"✅ {user}, your booking for {name.title()} is confirmed!"
            else:
                return f"❌ Sorry {user}, {name.title()} is fully booked."
    return "❗Please mention class name: Yoga / Zumba / HIIT"

def cancel_booking(user, text):
    for b in bookings:
        if b["user"] == user and b["class"] in text:
            bookings.remove(b)
            classes[b["class"]]["slots"] += 1
            return f"❌ {user}, your booking for {b['class'].title()} is cancelled."
    return "You don't have any such booking to cancel."

def view_bookings(user):
    user_bookings = [b["class"].title() for b in bookings if b["user"] == user]
    if not user_bookings:
        return "📭 No bookings found."
    return "📜 Your Bookings: " + ", ".join(user_bookings)

def chatbot_response(user, text):
    text = text.lower()

    if re.search(r"(hi|hello|hey)", text):
        return f"Hey {user}! 👋 Type 'show classes' to see available classes."

    if "show" in text and "class" in text:
        return show_classes()

    # ✅ Move this ABOVE 'book'
    if "my booking" in text or "my bookings" in text or "history" in text:
        return view_bookings(user)

    if "cancel" in text:
        return cancel_booking(user, text)

    if "book" in text:
        return book_class(user, text)

    return "🤖 Try commands like: 'show classes', 'book yoga', 'cancel yoga', 'my bookings'"
