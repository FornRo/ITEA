''' _________________________________________________________________ 72
2)Сгенерировать последовательность из случайных значений (случайного
размера). Найти корень квадратный от каждого числа в последовательности
используя функцию высшего порядка map. (функцию поиска корня от числа
используем из стадтартного модуля math). Найти медианное значение
последовательности. С помощью функции filter вывести все значения
последовательности корней квадратных, которые больше чем медианное
значение.
Пример
Входная последовательность [4, 16, 36, 49]
После поиска корней [2, 4, 6, 7]
Медиана = 5 ((4 + 6) / 2)
Результат [6, 7]
'''
import random
import math
import statistics

# random >> list[min(long), max(long)]


def generatn(long = 2):
    try:
        lst = []
        list(map(lambda gen: lst.append(random.randint(0, 100)), range(long)))
        return lst
    except:
        print("Что-то пошло не так")

def next_do(lst = [1, 4, 9, 16, 25, 36, 49, 64, 98, 100]):
    # квадрат
    lst = list(map(lambda x: math.sqrt(x), lst))
    return lst

my_lst = generatn(int(input()))
# my_lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] # test
my_lst = next_do(my_lst)
mediana = float(statistics.median(my_lst))

ans_finish = list(filter(lambda x: x > mediana, my_lst))
print(f'Медиана = {mediana}')
print(f'Результат = {ans_finish}')
# print(f'Результат', my_filter(my_sqrt(generation(int(input()))))


# print(generation(4))
# test = [4, 9, 16, 25, 36]
# print(my_sqrt(test))
