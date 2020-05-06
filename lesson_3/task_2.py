''' _________________________________________________________________ 72
Создать функцию которая будет вычислять сумму элементов
последовательности (list or tuple)
'''
my_lst = [1, 2, 3, 4, 5]  # sum 15
my_tpl = (1, 2, 3, 4, 5)


def nor_sum(lst):
    answ = 0
    for i in lst:
        answ += i
    return(answ)


print(nor_sum(my_lst))
print(nor_sum(my_tpl))