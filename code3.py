"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
digit_str = input('Введите число: ')
d1 = int(digit_str)
d2 = int(digit_str * 2)
d3 = int(digit_str * 3)

summ = d1 + d2 + d3
print(f'{d1} + {d2} + {d3} = {summ}')