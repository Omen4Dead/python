"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('file_for_code_1,2.txt', 'r', encoding='utf-8') as f:
    file = f.readlines()
    # print(file)  # проверка
row_count = len(file)
words_count = []
for i in file:
    i = i.strip()
    # print(i)  # проверка
    words = i.split()
    words_count.append(len(words))

print(f'Кол-во строк в файле: {row_count}')
print(f'Кол-во слов по строкам: ')
for num, count in enumerate(words_count, 1):
    print(num, '->', count)
