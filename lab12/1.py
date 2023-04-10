import os

filename = 'testfile.txt'
with open(filename, 'w', encoding='utf-8') as file:
    print(f'Файл {filename} создан.')

data = 'Тестовый текст!'
with open(filename, 'w', encoding='utf-8') as file:
    file.write(data)
    print(f'Данные записаны в файл {filename}.')

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    print(f'Содержимое файла {filename}:')
    print(content)

new_filename = 'renamedfile.txt'
os.rename(filename, new_filename)
print(f'Файл {filename} переименован в {new_filename}.')

os.remove(new_filename)
print(f'Файл {new_filename} удален.')
