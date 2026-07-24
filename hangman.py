# (იმფორთ რენდომ ბიბლიოთეკა)
import random

# (სთეიჯის - ნახატების სია მცდელობების მიხედვით)
STAGES = [
    """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
    =========
    """,  # 0 მცდელობა
    """
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
    =========
    """,  # 1 მცდელობა
    """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
    =========
    """,  # 2 მცდელობა
    """
        -----
        |   |
        O   |
       /|   |
            |
            |
    =========
    """,  # 3 მცდელობა
    """
        -----
        |   |
        O   |
        |   |
            |
            |
    =========
    """,  # 4 მცდელობა
    """
        -----
        |   |
        O   |
            |
            |
            |
    =========
    """,  # 5 მცდელობა
    """
        -----
        |   |
            |
            |
            |
            |
    =========
    """,  # 6 მცდელობა
]


# (დეფ ჰენგმენ - ფუნქციის შექმნა)
def hangman():
    print("\n--- 🔤 თამაში: Hangman ---")
    words = ["python", "program", "code", "developer", "backend"]
    
    # (რენდომის ჩოის ფუნქციით ირჩევს სიტყვას)
    secret_word = random.choice(words)
    
    # (გესდ ლეთერს - გამოცნობილი ასოების სია)
    guessed_letters = []
    attempts = 6

    # (უაილ ციკლი - სანამ მცდელობა მეტია 0-ზე)
    while attempts > 0:
        # (ბეჭდავს ნახატს დარჩენილი მცდელობის მიხედვით)
        print(STAGES[attempts])

        # (ფორ ციკლით აწყობს დაფარულ სიტყვას)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"სიტყვა: {display_word}")
        print(f"დარჩენილი მცდელობები: {attempts}")

        # (თუ ქვედა ტირე აღარ არის, მოიგო)
        if "_" not in display_word:
            print("\n🎉 გილოცავთ! თქვენ გამოიცანით სიტყვა!")
            return

        # (ინფუთით იღებს ასოს, ლოუერით გადაყავს პატარა ასოში, სთრიფით აშორებს სფეისებს)
        guess = input("\nშეიყვანეთ ასო: ").lower().strip()

        # (ლენით და ისალფათი ვამოწმებთ, რომ იყოს მხოლოდ 1 ასო)
        if len(guess) != 1 or not guess.isalpha():
            print("❌ შეიყვანეთ მხოლოდ ერთი ასო!")
            continue  # (ქონთინიუთი გადადის ახალ წრეზე)

        # (ამოწმებს, უკვე იყო თუ არა ეს ასო)
        if guess in guessed_letters:
            print("⚠️ ეს ასო უკვე გამოყენებული გაქვთ.")
            continue

        # (აფენდით ამატებს ასოს სიაში)
        guessed_letters.append(guess)

        # (თუ არასწორი ასოა, აკლებს 1 მცდელობას)
        if guess not in secret_word:
            attempts -= 1
            print("❌ არასწორი ასოა!")

    # (თუ მცდელობა 0 გახდა - წააგო)
    print(STAGES[0])
    print(f"❌ წააგეთ! დაფარული სიტყვა იყო: {secret_word}")


if __name__ == "__main__":
    hangman()