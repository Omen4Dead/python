"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open('file_for_code_3.txt', encoding='utf-8') as f:
    lines = f.readlines()
all_salary = 0
base = {}

for line in lines:
    couple = line.split()
    base[couple[0]] = float(couple[1])

print(base)

for key, value in base.items():
    if value < 20000:
        print(f'Зарплата менее 20 тыс.: {key}')
    all_salary = all_salary + value

average_salary = round(all_salary / len(base), 2)
print(f'Средняя величина дохода сотрудников: {average_salary}')
