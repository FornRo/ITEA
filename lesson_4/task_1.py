''' _________________________________________________________________ 72
Написать программу которая принимает от пользователя строку из
разделенных запятой значений, на основе которой программа сформирует
кортеж и список из этих значений.
'''

def main():
    lst = []
    lst = input().split(', ')
    tpl = tuple(lst)
    print(lst)
    print(tpl)
main()
