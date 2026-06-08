import random
import re

# ---------------------------------------------------------------------------
# Response rules: each entry is (pattern, list_of_replies)
# The first pattern that matches the user's input is used.
# ---------------------------------------------------------------------------
RULES = [
    # Greetings
    (r"\b(hello|hi|hey|howdy|hiya|sup)\b",
     ["Hi there! 😊", "Hey! How can I help you?", "Hello! Nice to meet you."]),

    # How are you
    (r"\bhow are you\b|\bhow('re| are) you doing\b|\bwhat'?s up\b",
     ["I'm doing great, thanks for asking! How about you?",
      "All good on my end! What can I do for you?",
      "Feeling fantastic! What's on your mind?"]),

    # User says they're good
    (r"\bi('?m| am) (good|great|fine|okay|ok|well|fantastic|awesome)\b",
     ["Glad to hear that! 😊", "That's awesome!", "Wonderful!"]),

    # User says they're not well
    (r"\bi('?m| am) (bad|sad|not good|not okay|not ok|terrible|awful|down)\b",
     ["Oh no, I'm sorry to hear that. 😟 Hope things get better soon!",
      "That's tough. Want to talk about it?",
      "Sending good vibes your way! 💙"]),

    # Name
    (r"\bwhat'?s? your name\b|\bwho are you\b",
     ["I'm PyBot, your friendly Python chatbot! 🤖",
      "They call me PyBot. What's your name?"]),

    # User gives their name
    (r"\bmy name is (\w+)\b|\bi('?m| am) (\w+)\b",
     ["Nice to meet you! 😊", "Great name!", "Hello! It's a pleasure."]),

    # Time / date (bot can't really know, but responds politely)
    (r"\bwhat time is it\b|\bwhat'?s the (time|date)\b",
     ["I don't have a clock, but your device does! ⏰",
      "I can't check the time, but your phone knows!"]),

    # Jokes
    (r"\btell me a joke\b|\bsay something funny\b|\bjoke\b",
     ["Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
      "Why was the Python developer broke? Because he used all his cache! 💸",
      "How do you comfort a JavaScript bug? You console it. 😄"]),

    # Thanks
    (r"\b(thanks|thank you|thx|cheers)\b",
     ["You're welcome! 😊", "Anytime!", "Happy to help!"]),

    # Bye / exit
    (r"\b(bye|goodbye|see you|exit|quit|later|cya)\b",
     ["Goodbye! Have a great day! 👋", "See you later! 😊", "Bye! Take care!"]),

    # Help
    (r"\bhelp\b|\bwhat can you do\b",
     ["I can chat with you! Try saying: 'hello', 'tell me a joke', "
      "'how are you', or 'bye'. 😊"]),

    # Age
    (r"\bhow old are you\b|\bwhat'?s your age\b",
     ["I'm ageless — I'm a bot! ♾️", "Age is just a number, and I have none. 😄"]),

    # Weather
    (r"\bweather\b|\bwill it rain\b",
     ["I can't check the weather, but try weather.com! ☀️🌧️"]),
]

FALLBACKS = [
    "Hmm, I'm not sure I understand. Could you rephrase that?",
    "Interesting... I don't have a great answer for that one. 🤔",
    "I'm still learning! Try asking me something else.",
    "That's beyond my current knowledge. 😅",
]


def get_reply(user_input):
    text = user_input.strip().lower()
    for pattern, replies in RULES:
        if re.search(pattern, text):
            return random.choice(replies)
    return random.choice(FALLBACKS)


def main():
    print("=" * 40)
    print("       PyBot — Simple Chatbot        ")
    print("  (type 'bye' or 'quit' to exit)     ")
    print("=" * 40)

    while True:
        try:
            user = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPyBot: Goodbye! 👋")
            break

        if not user:
            continue

        reply = get_reply(user)
        print(f"PyBot: {reply}")

        # Exit on farewell
        if re.search(r"\b(bye|goodbye|exit|quit|cya|later)\b", user.lower()):
            break


if __name__ == "__main__":
    main()
