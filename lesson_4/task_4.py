''' _________________________________________________________________ 72
4) Создать программу, которая будет вычислять суму 
всех вложенных списков. Размерность, значения,
и количество вложенных списков должны генерироваться случайным
образом (модуль random).

Например сгенерирован случайный список [[3, 4, 10], [1, 2]], 
результатом должно быть: 20. (3 + 4 + 10 + 1 + 2). Уровень вложенности 1.
'''


def main(my_lst):
    answer = 0
    for target_list in my_lst:
        for i in target_list:
            answer += i
    return(answer)


print(main([[3, 4, 10], [1, 2]]))
