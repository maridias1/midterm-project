def atm():
    balance = 100.0

    while True:
        print("\n=== 🏧 ATM ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Return to Main Menu")

        choice = input("Select an operation (1-4): ").strip()

        if choice == "1":
            print(f"\n💰 Your current balance is: {balance:.2f} ₾")

        elif choice == "2":
            try:
                amount = float(input("\nEnter deposit amount: "))
                if amount > 0:
                    balance += amount
                    print(
                        f"✅ Successfully deposited {amount:.2f} ₾. New balance: {balance:.2f} ₾"
                    )
                else:
                    print("❌ Amount must be a positive number!")
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == "3":
            try:
                amount = float(input("\nEnter withdrawal amount: "))
                if amount > balance:
                    print("❌ Insufficient funds!")
                elif amount <= 0:
                    print("❌ Amount must be a positive number!")
                else:
                    balance -= amount
                    print(
                        f"✅ Withdrawn {amount:.2f} ₾. Remaining balance: {balance:.2f} ₾"
                    )
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == "4":
            print("\nATM session ended. 👋")
            break

        else:
            print("❌ Invalid choice! Please select between 1 and 4.")
