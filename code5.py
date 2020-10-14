"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('file_for_code_5.txt', 'w+', encoding='utf-8') as file:
    file.write(input())
    file.seek(0)
    f = file.read()
    numbers = f.split()
    print(numbers)
    numbers = map(float, numbers)
    all_sum = sum(numbers)
    print(all_sum)
