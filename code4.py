"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
digit = input('Введите число: ')
count = 0
maximum = 0

while count < len(digit):
    if maximum < int(digit[count]):
        maximum = int(digit[count])
    count += 1
print('Самая большая цифра в числе: ', maximum)
