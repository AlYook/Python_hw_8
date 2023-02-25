"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def line_n_word_count():
    lines_count = 0

    with open('task_2.txt', 'r') as f:

        for num, line in enumerate(f, start=1):
            print(f'Количество слов в {num} строке: {len(line.split())}')
            lines_count += line.count('\n')
    
    print(f'Общее количество строк: {lines_count}')


line_n_word_count()
