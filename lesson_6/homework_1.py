''' _________________________________________________________________ 72
1) Создать декоратор который будет сохранять возвращаемый результат любой
функции в программе и будет записывать его в файл logs.txt в формате :
ВремяИДатаВызоваФункции:РезультатВыполненияФункции.
'''

import time


def main(func):
    with open("lesson_6\\long.txt", 'a', encoding="utf-8") as file:
        file.write(f'{time.strftime("%x | %X")} : {func} \n')

# sum()


def func_sum(lst):
    lst, ans = list(lst), 0
    for i in lst:
        ans += float(i)
    return ans


st = '12345'
main(func_sum(st))


# math.pow(a, b)
def func_pow(a, b):
    return a ** b


main(func_pow(5, 2))
