"""
3) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


def num_swap():
    swap_map = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

    with open('task_3.txt', 'r') as f:

        for line in f:
            line_list = line.split(' - ')

            if line_list[0] in swap_map:
                swapped_num = swap_map[line_list[0]]

            with open('task_3_solve.txt', 'a', encoding='utf-8') as new_file:
                new_file.writelines(swapped_num + ' - ' + line_list[1])


num_swap()
