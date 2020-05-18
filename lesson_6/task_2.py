''' _________________________________________________________________ 72
2) Написать функцию которая будет генерировать пароль из случайного набора
символов фиксированной длинны. Каждый новый пароль должен сохраняться в
файл в режиме «append»
'''
import random

def write_pass_in_file(pass_w):
    with open("lesson_6\\passwords.txt", 'a',  encoding="utf-8") as file:
        file.write(f'{pass_w} \n')


def generaion_pass():
    strs = r'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@_'
    pass_word = ''
    # 15's symbol in pass
    for _ in range(16):
        letter = random.randint(0, 85)
        pass_word += strs[letter]
    return pass_word


write_pass_in_file(generaion_pass())

