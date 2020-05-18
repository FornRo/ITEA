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


# random >> list[min(long), max(long)]
def generation(long):
    lst = []
    list(map(lambda gen: lst.append(random.randint(0, 100)), range(long)))
    return lst
    # for target_list in range(long):
    #    lst.append(random.randint(0, 100))
    # return lst


def my_sqrt(my_list):  # 2 ** 2
    print(list(map(lambda x: math.sqrt(x), my_list)))
    return list(map(lambda x: math.sqrt(x), my_list))


def my_filter(lst):  # filter
    ans = []
    for i in lst:
        if i > (sum(lst) / len(lst)):
            ans.append(i)
    print(ans)
    return ans


ans_gnrt = generation(int(input()))
ans_sqrt = my_sqrt(ans_gnrt)
ans_filtre = filter(lambda x: i > (sum(lst / len(lst))))
print(f'Медиана = {}')
print(f'Результат = {ans_filtre}'
# print(f'Результат', my_filter(my_sqrt(generation(int(input()))))


# print(generation(4))
# test = [4, 9, 16, 25, 36]
# print(my_sqrt(test))
