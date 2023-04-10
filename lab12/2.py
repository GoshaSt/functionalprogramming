
def read_names_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        names = [line.strip() for line in file.readlines()]
    return names

def check_name_in_lists(name, girl_names, boy_names):
    girl_name_found = name in girl_names
    boy_name_found = name in boy_names

    if girl_name_found and boy_name_found:
        return "both"
    elif girl_name_found:
        return "girl"
    elif boy_name_found:
        return "boy"
    else:
        return "none"

girl_names_filename = 'GirlNames.txt'
boy_names_filename = 'BoyNames.txt'

girl_names = read_names_from_file(girl_names_filename)
boy_names = read_names_from_file(boy_names_filename)

name1 = input("Введите первое имя (или оставьте пустым): ").strip()
name2 = input("Введите второе имя (или оставьте пустым): ").strip()

if name1:
    result1 = check_name_in_lists(name1, girl_names, boy_names)
    if result1 == "both":
        print(f"Имя {name1} находится в обоих списках.")
    elif result1 == "girl":
        print(f"Имя {name1} находится в списке имён девочек.")
    elif result1 == "boy":
        print(f"Имя {name1} находится в списке имён мальчиков.")
    else:
        print(f"Имя {name1} не находится ни в одном из списков.")

if name2:
    result2 = check_name_in_lists(name2, girl_names, boy_names)
    if result2 == "both":
        print(f"Имя {name2} находится в обоих списках.")
    elif result2 == "girl":
        print(f"Имя {name2} находится в списке имён девочек.")
    elif result2 == "boy":
        print(f"Имя {name2} находится в списке имён мальчиков.")
    else:
        print(f"Имя {name2} не находится ни в одном из списков.")
