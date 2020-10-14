"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
with open('file_for_code_7.txt', 'rt', encoding='utf-8') as f:
    file = f.readlines()
lines = []
base = {}
profits = []

for i in file:
    lines.append(i.strip().split())

for obj in lines:
    print(obj)
    profit = int(obj[2]) - int(obj[3])
    base[obj[0]] = profit
    if profit > 0:
        profits.append(profit)

average_profit = sum(profits)
print(base)
result = [base, {'average_profit': average_profit}]
print(result)

with open('file_for_code_7_new.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
