''' _________________________________________________________________ 72
Создать функцию которая будет принимать 2 числовых значения,
возвращать True если они равны, или их сумма или разница равна 5.
'''


def Turn_off(first, second):
    if first == second:
        print(True)
    elif (float(first) + float(second) == 5):
        print(True)
    elif (float(first) - float(second) == 5):
        print(True)
    else:
        print(False)


Turn_off(input(), input())        