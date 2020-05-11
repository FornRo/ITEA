# ___________________________________________________________________ 72
# \t TAB # \n Enter # \v 
# r'Hello \n and \v and \t'

'''
file = open('text.txt', encoding='utf-8')
читать файл
print(file.read()) # ошпка "_"

for line in file:
    print(line.strip())
'''
'''
file = open('text.txt', 'w', encoding='utf-8')

for i in range(55, 70):
    file.write(str(i))

'''
file = open('lesson_3\task_1.py', 'r', encoding='utf-8')
r = file.readlines()
print(r)
file.close()
