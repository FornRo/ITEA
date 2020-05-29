# Приложение записной книги из урока 7 через консоль.
# Пользователя спрашивает хочет ли он ввести контакт (введите 1) или 
# посмотреть записную книгу (введите 2) или
# выйти (введите 3).
# Если (1), то вводит следующую информацию :
# [время] Имя, Фамилия, Номер телефона, Адрес.
# контакт должен записываться в json файл,
# После введения контакта повторяется первый запрос.
# При выбора (2) чтение json файла в консоль. 
# В конце предлагает Очистить список (введите 1) или выйти (введите 2).
# При введеной 1 файл будет очищаться и завершаться работа программы.
# При введеной 2 завершается работа программы.

import json
from time import strftime


def write_mod(): # (1)
    dict_entry = {
        'Time': strftime('%X'),
        'Name': input('Name :'), 
        'Surname': input('Surname :'), 
        'Number_phone':input('Number_phone :'), 
        'Adres': input('Adres :')
    }
    print()
    dict_entry = json.dumps(dict_entry)
    with open(r"lesson_8\Bas_Data.json", 'a', encoding='utf-8') as file:
        file.write(f"{dict_entry} \n")


def read_mod(): # (2)
    with open(r"lesson_8\Bas_Data.json", 'r', encoding='utf-8') as file:
        for i in file:
            print(i.strip())
        print()
    
    print('**Clear the notebook**') # Очистить список (1) / (2).
    x = input('*Yes = 1, no = 2 *\n')
    if x == '1':
        with open(r"lesson_8\Bas_Data.json", 'w', encoding='utf-8') as file:
            file.write('')


# ______________________________________________________________________
# __main__
if __name__ == "__main__":
    while True:
        mode = input(
            ' **Enter contact = 1, view notebook = 2, exit = 3 **\n'
        )

        if mode == '1': # ввести контакт (1)
            write_mod()
        elif mode == '2': # посмотреть записную книгу (2)
            read_mod()
            break
        elif mode == '3': # выйти (3)
            break
# ______________________________________________________________________