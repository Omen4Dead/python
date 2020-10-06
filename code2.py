"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def person(name, surname, year, city, email, phone):
    print(f'Name - {name} {surname}, Year of birth - {year}, City - {city}, Email - {email}, Phone Number - {phone}')


person(surname='Petrov', year=1992, name='Petr', email='example@mail.ru', phone='89991234567', city='Moscow')
