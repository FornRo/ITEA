# ___________________________________________________________________ 72
# \t TAB # \n Enter # \v 
# r'Hello \n and \v and \t'

file = open('lesson_3\\task_1.py', 'r', encoding='utf-8')
r = file.readlines() #  = lst(file)
print(r)
file.close()
'''
# ___________________________time____________________________________ 72
import time
print(time.time())
print(time.ctime())
print(
    time.strftime('number %d mothe %m', time.localtime())
    )
'''