''' _________________________________________________________________ 72
2) Написать функцию которая будет генерировать пароль из случайного набора
символов фиксированной длинны. Каждый новый пароль должен сохраняться в
файл в режиме «append»
'''
import random
import string


def write_pass_in_file(pass_w):
    with open("lesson_6\\passwords.txt", 'a',  encoding="utf-8") as file:
        file.write(pass_w)


def generaion_pass():
    pass_word = ''
    # 15's symbol in pass
    for symbol in range(16):
        letter = random.randint(0, 99)
        pass_word += string.printable[letter]
    return pass_word


print(string.printable)
write_pass_in_file(generaion_pass())
