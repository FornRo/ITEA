''' _________________________________________________________________ 72
Создать функцию которая будет принимать 2 числовых значения,
возвращать True если они равны, или их сумма или разница равна 5.
'''


def Turn_off(first, second):
    first, second = float(first), float(second)
    if first == second:
        return True 
    elif (abs(first + second) == 5):
        return True
    elif (abs(first - second) == 5):
        return True
    else:
        return False


print(Turn_off(input(), input()))