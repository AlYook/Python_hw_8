"""
1) Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def write_input():
    text_line = input('Введите какой-нибудь текст: ')

    if not text_line:
        return
    
    
    with open('task_1.txt', 'a', encoding='utf-8') as f:
        f.write(text_line + '\n')

    return write_input() 


write_input()
