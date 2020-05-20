''' _________________________________________________________________ 72
1) Создать декоратор который будет сохранять возвращаемый результат любой
функции в программе и будет записывать его в файл logs.txt в формате :
ВремяИДатаВызоваФункции:РезультатВыполненияФункции.
'''

import time

def decorator(func):
    def wrapper(arg1):
        with open("lesson_6\\long.txt", 'a', encoding="utf-8") as file:
            file.write(f'{time.strftime("%x | %X")} : {func(arg1)} \n')
        result = func(arg1)
        return result
    return wrapper

# sum()
@decorator
def func_sum(lst):
    lst, ans = list(lst), 0
    for i in lst:
        ans += float(i)
    return ans


st = '12345'
func_sum(st)


# math.pow(a, b)
@decorator
def func_pow(a):
    return a ** 2

func_pow(5)