''' _________________________________________________________________ 72
Написать программу которая принимает от пользователя строку из
разделенных запятой значений, на основе которой программа сформирует
кортеж и список из этих значений.
'''
import collections

lst = [1, 1, 1, 3, 2, 4, 4, 4, 10, 10, 10, 10, 10] #lst  = input()
c = collections.Counter()
for word in lst:
    c[word] += 1
print(c)
print(list(c))

# print(collections.Counter('abracadabra').most_common(3))