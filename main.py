import calculator
import guess_number
import hangman
import translator
import atm


def main():
    while True:
        print("\n" + "=" * 35)
        print("       Main Menu - Project       ")
        print("=" * 35)
        print("1. Calculator")
        print("2. Guess the Number")
        print("3. Hangman")
        print("4. Translator")
        print("5. ATM")
        print("6. Exit")
        print("=" * 35)

        choice = input("Select an operation (1-6): ").strip()

        if choice == "1":
            calculator.calculator()
        elif choice == "2":
            guess_number.guess_number()
        elif choice == "3":
            hangman.hangman()
        elif choice == "4":
            translator.translator()
        elif choice == "5":
            atm.atm()
        elif choice == "6":
            print("\nProgram ended. Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice! Please select between 1 and 6.")


if __name__ == "__main__":
    main()
