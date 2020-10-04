"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
number = int(input('Введите месяц: '))
# решение через list
lst = ['Зима', 'Весна', 'Лето', 'Осень']
if number == 12 or number == 1 or number == 2:
    print(lst[0])

if number == 3 or number == 4 or number == 5:
    print(lst[1])

if number == 6 or number == 7 or number == 8:
    print(lst[2])

if number == 9 or number == 10 or number == 11:
    print(lst[3])
# решение через dict
dct = {'Зима': [12, 1, 2],
       'Весна': [3, 4, 5],
       'Лето': [6, 7, 8],
       'Осень': [9, 10, 11]}

for key, value in dct.items():
    if number in value:
        print(key)
