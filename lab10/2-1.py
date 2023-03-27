def unique_chars(string):
    unique_chars = set(string)
    sorted_chars = sorted(list(unique_chars))
    print("Уникальные символы в строке:", ", ".join(sorted_chars))

string = input("Введите строку: ")
unique_chars(string)
