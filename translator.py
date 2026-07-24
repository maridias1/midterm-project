# (იმფორთ ო-ეს - ფაილურ სისტემასთან სამუშაოდ)
import os


# (დეფ თრანსლეითორ - ფუნქცია)
def translator():
    print("\n--- 📖 თარჯიმანი ---")
    file_name = "dictionary.txt"

    # (ო-ეს ბიბლიოთეკის ექსისტს ფუნქციით ამოწმებს არსებობს თუ არა ფაილი)
    if not os.path.exists(file_name):
        # (უიზ ოფენ 'w' რეჟიმით - ქმნის ფაილს)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("apple:ვაშლი\nbook:წიგნი\ncode:კოდი\n")

    # (ინფუთით იღებს სიტყვას, სთრიფით და ლოუერით ამუშავებს)
    word_to_find = (
        input("შეიყვანეთ ინგლისური სიტყვა სათარგმნად: ").strip().lower()
    )

    # (დიქშენარი - ცარიელი ლექსიკონი)
    dictionary = {}
    
    # (უიზ ოფენ 'r' რეჟიმით - კითხულობს ფაილს)
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                # (სფლითით ყოფს ინგლისურ და ქართულ ნაწილებად)
                eng, geo = line.strip().split(":")
                dictionary[eng] = geo

    # (ამოწმებს არის თუ არა სიტყვა ლექსიკონში)
    if word_to_find in dictionary:
        print(f"✅ თარგმანი: {dictionary[word_to_find]}")
    else:
        print("❌ სიტყვა ვერ მოიძებნა.")
        add_new = (
            input("გსურთ ამ სიტყვის დამატება? (კი/არა): ").strip().lower()
        )
        if add_new == "კი":
            translation = input(f"შეიყვანეთ '{word_to_find}'-ის თარგმანი: ")
            # (უიზ ოფენ 'a' რეჟიმით - ამატებს ფაილის ბოლოში)
            with open(file_name, "a", encoding="utf-8") as f:
                f.write(f"{word_to_find}:{translation}\n")
            print("✅ დაემატა ფაილში!")


if __name__ == "__main__":
    translator()