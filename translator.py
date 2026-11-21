import os


def translator():
    print("\n--- 📖 Translator ---")
    file_name = "dictionary.txt"

    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("apple:a round fruit with red or green skin\nbook:a written or printed work consisting of pages\ncode:program instructions written in a programming language\n")

    word_to_find = (
        input("Enter a word to translate: ").strip().lower()
    )

    dictionary = {}
    
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                word, meaning = line.strip().split(":", 1)
                dictionary[word] = meaning

    if word_to_find in dictionary:
        print(f"✅ Translation: {dictionary[word_to_find]}")
    else:
        print("❌ Word not found.")
        add_new = (
            input("Would you like to add this word? (yes/no): ").strip().lower()
        )
        if add_new == "yes":
            translation = input(f"Enter the translation/meaning for '{word_to_find}': ")
            with open(file_name, "a", encoding="utf-8") as f:
                f.write(f"{word_to_find}:{translation}\n")
            print("✅ Added to the file!")


if __name__ == "__main__":
    translator()
