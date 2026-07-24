import calculator
import guess_number
import hangman
import translator
import atm


def main():
    while True:
        print("\n" + "=" * 35)
        print("       მთავარი მენიუ - პროექტი    ")
        print("=" * 35)
        print("1. კალკულატორი")
        print("2. გამოიცანი რიცხვი")
        print("3. ჰენგმენი (ჩამოხრჩობანა)")
        print("4. თარგმანი")
        print("5. ბანკომატი")
        print("6. გამოსვლა")
        print("=" * 35)

        choice = input("აირჩიეთ ოპერაცია (1-6): ").strip()

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
            print("\nპროგრამა დასრულდა. ნახვამდის! 👋")
            break
        else:
            print("\n❌ არასწორი არჩევანი! გთხოვთ აირჩიოთ 1-დან 6-მდე.")


if __name__ == "__main__":
    main()