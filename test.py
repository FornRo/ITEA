# ___________________________________________________________________ 72
import collections


def main(my_lst):
    my_dict = dict(collections.Counter(my_lst))
    max_key, max_number = 0, 0

    for nbr in my_dict.items():
        if (((nbr[0] > max_key) and (nbr[1] >= max_number)) or
            (nbr[1] > max_number)
            ):
            max_key = nbr[0]
            max_number = nbr[1]
        print(nbr)

    print('max_key =', max_key)
    print('max_number', max_number)
    print(f'Элемент который чаще всего повторяется {max_key}')


inpt = [0, 0, 4, 4, 1, 1, 3, 2]  # lst  = input()

# main(inpt)
a = input()
print(type(a))
print(a)
