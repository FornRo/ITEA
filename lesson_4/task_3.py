''' _________________________________________________________________ 72
3) Создать функцию которая будет принимать случайную числовую 
последовательность и будет возвращать элемент который чаще всего
повторяется в этой последовательности. Если таких элементов несколько 
возвращать самый большой.

№ 3) на входе [1, 1, 1, 3, 2, 4, 4, 4] на выходе цифра 4. 
т.к. 1 и 4 повторяются по 3 раза,
но 4 больше чем 1 по этому результат - 4
'''

lst = [1, 1, 1, 3, 2, 4, 4, 4] #lst  = input()
ans = lst[0], 0
lst = sorted(lst)
print(sorted(lst))



'''
for i in lst:
    if i == wd:
        cop +=1
    elif i != wd:
        print(str(wd) + str(cop), end='') 
        wd, cop = i, 1
print(str(wd) + str(cop), end='')

# a4b2c1a2
'''