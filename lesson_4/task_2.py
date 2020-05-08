''' _________________________________________________________________ 72
Создать функцию которая будет вычислять сумму всех цифр числа.
Например на входе 1234, на выходе должно быть:
10, т. к. 1 + 2 + 3 + 4 = 10.
'''

def sum_main(numbers):
    ans = 0
    i = 0
    while i <= len(numbers):
        # end 
        if i == len(numbers):
            print(numbers[i-1], '=', ans)
            break
        # sum answer 
        ans += int(numbers[i]) 
        # start 
        if i == 0:
            print(numbers[i], '+', end = ' ')
        # mid
        elif (i != len(numbers)) and (i != len(numbers)-1):
            print(numbers[i], '+', end = ' ')
        i += 1


sum_main(input())