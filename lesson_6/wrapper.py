# ___________________________________________________________________ 72


def my_decorator(lst):

    def wrapper():
        print('Decoration')
        lst, ans = list(lst), 0
        for i in lst:
            ans += float(i)
        print('End of decoration')
        with open("lesson_6\\long.txt", 'a', encoding="utf-8") as file:
            file.write(f'{time.strftime("%x | %X")} : {ans} \n')

        return ans
    return wrapper


@my_decorator
def exmp():
    print('Write')


exmp(my_decorator(lst='123345'))
