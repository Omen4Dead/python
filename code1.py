"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
lst = [True, 1, 3.25, 'hello', 1-2j]

for i in lst:
    print(f'{i} -> {type(i)}')
