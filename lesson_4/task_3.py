''' _________________________________________________________________ 72
3) Создать функцию которая будет принимать случайную числовую 
последовательность и будет возвращать элемент который чаще всего
повторяется в этой последовательности. Если таких элементов несколько 
возвращать самый большой.

№ 3) на входе [1, 1, 1, 3, 2, 4, 4, 4] на выходе цифра 4. 
т.к. 1 и 4 повторяются по 3 раза,
но 4 больше чем 1 по этому результат - 4
'''

import collections


def main(my_lst):
    my_dict = dict(collections.Counter(my_lst))
    max_key, max_series = 0, 0

    for nbr in my_dict.items():
        if (((nbr[0] > max_key) and (nbr[1] >= max_series)) or
            (nbr[1] > max_series)
            ):
            max_key = nbr[0]
            max_series = nbr[1]
        print(nbr)

    print(f'max число = {max_key}, max series = {max_series}')
    print(f'Элемент который чаще всего повторяется {max_key}')


inpt = [0, 0, 4, 4, 1, 1, 3, 2]  # lst  = input()

main(inpt)
