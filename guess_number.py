import random


def guess_number():
    print("\n--- 🎲 Guess the Number ---")
    
    target = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter a number (1-100): "))
            attempts += 1

            if guess < target:
                print("📈 Higher!")
            elif guess > target:
                print("📉 Lower!")
            else:
                print(
                    f"🎉 You guessed it! The number was {target}. Attempts: {attempts}"
                )
                break
        
        except ValueError:
            print("❌ Please enter a whole number!")


if __name__ == "__main__":
    guess_number()
