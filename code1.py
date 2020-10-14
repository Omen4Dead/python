"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('file_for_code_1,2.txt', 'w', encoding='utf-8') as first_file:
    while True:
        line = input()
        if line == '':
            break
        else:
            first_file.write(line + '\n')
