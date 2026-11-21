def calculator():
    print("\n--- 🧮 Calculator ---")
    
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Select an operation (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("❌ Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("❌ Invalid operator!")
            return

        print(f"✅ Result: {result}")

    except ValueError:
        print("❌ Please enter numbers only!")


if __name__ == "__main__":
    calculator()
