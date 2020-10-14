"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
new_lines = []
with open('file_for_code_4.txt', 'r', encoding='utf-8') as file:  # 'r' для наглядности
    lines = file.readlines()

for line in lines:
    if 'One' in line:
        new_lines.append(line.replace('One', 'Один'))
    elif'Two' in line:
        new_lines.append(line.replace('Two', 'Два'))
    elif 'Three' in line:
        new_lines.append(line.replace('Three', 'Три'))
    elif 'Four' in line:
        new_lines.append(line.replace('Four', 'Четыре'))
print(new_lines)

with open('file_for_code_4_new.txt', 'w', encoding='utf-8') as f:
    for i in new_lines:
        f.write(i)
