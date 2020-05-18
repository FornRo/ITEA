''' _________________________________________________________________ 72
3) Создать функцию которая генерирует список из 100 тыс. случайных 
элементов в диапазоне [0, 1000] и вывести на экран время 
выполнения этой функции.
'''

import random
import time


def main():
    my_lst = []
    for target_list in range(10 ** 5):
        my_lst.append(random.randint(0, 1000))
    print(len(my_lst))

start_time = time.time()
main()
print('this take for', round(time.time() - start_time, 4), 'second')
