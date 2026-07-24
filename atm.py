def atm():
    balance = 100.0  # საწყისი ბალანსი

    while True:
        print("\n=== 🏧 ბანკომატი ===")
        print("1. ბალანსის შემოწმება")
        print("2. თანხის შეტანა")
        print("3. თანხის გამოტანა")
        print("4. მთავარ მენიუში დაბრუნება")

        choice = input("აირჩიეთ ოპერაცია (1-4): ").strip()

        if choice == "1":
            print(f"\n💰 თქვენი მიმდინარე ბალანსია: {balance:.2f} ₾")

        elif choice == "2":
            try:
                amount = float(input("\nშეიყვანეთ შესატანი თანხა: "))
                if amount > 0:
                    balance += amount
                    print(
                        f"✅ წარმატებით დაემატა {amount:.2f} ₾. ახალი ბალანსი: {balance:.2f} ₾"
                    )
                else:
                    print("❌ თანხა უნდა იყოს დადებითი რიცხვი!")
            except ValueError:
                print("❌ გთხოვთ შეიყვანოთ სწორი ციფრი!")

        elif choice == "3":
            try:
                amount = float(input("\nშეიყვანეთ გამოსატანი თანხა: "))
                if amount > balance:
                    print("❌ ანგარიშზე არ არის საკმარისი თანხა!")
                elif amount <= 0:
                    print("❌ თანხა უნდა იყოს დადებითი რიცხვი!")
                else:
                    balance -= amount
                    print(
                        f"✅ გამოტანილია {amount:.2f} ₾. დარჩენილი ბალანსი: {balance:.2f} ₾"
                    )
            except ValueError:
                print("❌ გთხოვთ შეიყვანოთ სწორი ციფრი!")

        elif choice == "4":
            print("\nბანკომატით მომსახურება დასრულებულია. 👋")
            break

        else:
            print("❌ არასწორი არჩევანი! გთხოვთ აირჩიოთ 1-დან 4-მდე.")