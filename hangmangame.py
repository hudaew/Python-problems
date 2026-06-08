import random

WORDS = ["python", "hangman", "keyboard", "science", "program"]

STAGES = [
    """
  -----
  |   |
      |
      |
      |
      |
=========""",
    """
  -----
  |   |
  O   |
      |
      |
      |
=========""",
    """
  -----
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  -----
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  -----
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def play_hangman():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0
    max_wrong = 6

    print("\n=============================")
    print("       HANGMAN GAME          ")
    print("=============================")

    while wrong < max_wrong:
        display = " ".join(letter if letter in guessed else "_" for letter in word)

        print(STAGES[wrong])
        print(f"\nWord:  {display}")
        print(f"Wrong guesses ({wrong}/{max_wrong}): {', '.join(sorted(guessed)) if guessed else '-'}")

        if "_" not in display:
            print(f"\n✅  You WIN! The word was: '{word}'")
            return

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠  Please enter a single letter.")
            continue

        if guess in guessed:
            print("⚠  Already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"✅  '{guess}' is in the word!")
        else:
            wrong += 1
            print(f"❌  '{guess}' is NOT in the word.")

    print(STAGES[max_wrong])
    print(f"\n💀  Game over! The word was: '{word}'")


if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! Goodbye.")
            break
