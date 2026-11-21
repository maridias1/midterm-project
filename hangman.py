import random

STAGES = [
    """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
    =========
    """,
    """
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
    =========
    """,
    """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
    =========
    """,
    """
        -----
        |   |
        O   |
       /|   |
            |
            |
    =========
    """,
    """
        -----
        |   |
        O   |
        |   |
            |
            |
    =========
    """,
    """
        -----
        |   |
        O   |
            |
            |
            |
    =========
    """,
    """
        -----
        |   |
            |
            |
            |
            |
    =========
    """,
]


def hangman():
    print("\n--- 🔤 Game: Hangman ---")
    words = ["python", "program", "code", "developer", "backend"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(STAGES[attempts])

        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"Word: {display_word}")
        print(f"Remaining attempts: {attempts}")

        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word!")
            return

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("⚠️ You have already used this letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("❌ Wrong letter!")

    print(STAGES[0])
    print(f"❌ You lost! The secret word was: {secret_word}")


if __name__ == "__main__":
    hangman()
