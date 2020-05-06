''' _________________________________________________________________ 72
Создать список из N целочисленных случайных значений. N — количество,
которое вводит с клавиатуры пользователь. Используя цикл for вывести все
четные числа этого списка, если таковых нет вывести на экран
соответствующее сообщение.
'''
import random

def main(n):
    lst = []
    for target_list in range(n):
        lst.append(int(random.randint(0, 999)))
    print(lst)
    
    parity_chk = False # Проверка на отсутствия четности 

    for i in range(n):
        if lst[i] % 2 == 0:
            print('Четное число', lst[i])
            parity_chk = True
            
    if parity_chk == False:
        print('нет четных чисел ')

main(int(input()))