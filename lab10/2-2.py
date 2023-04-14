elements = [1, 2, 'String', 4, 'String2', 6, 7, 8, 9, 10]

if any(isinstance(element, int) for element in elements):
    print("В списке есть числовые значения")
else:
    print("В списке нет числовых значений")

if all(isinstance(element, int) for element in elements):
    print("Все элементы в списке числовые значения")
else:
    print("Не все элементы в списке числовые значения")
