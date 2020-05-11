# ___________________________________________________________________ 72


def sum_main(numbers):
    sum_ans, multiply_ans = 0, int(numbers[0])
#    for i in numbers:
    i = 0
    while i <= len(numbers):
        i +=1 
        # sum answer
        sum_ans += int(numbers[i])
        if i != 1:
            pass
        # multiplication answer
        multiply_ans *= int(numbers[i])

    print('Сумма цифр =', sum_ans)
    print('Произведение цифр =', multiply_ans)
sum_main(input())

