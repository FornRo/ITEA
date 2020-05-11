''' _________________________________________________________________ 72
1) Создать программу которая будет создавать копию самой себя. Копия
программы должна сохраняться рядом с исходной программой под
именем script_copy.
'''
file =  open("task_1.py", 'r',)
original_file = file
file = open('copy_file.txt', 'w')

for target_list in original_file:
    file.write(target_list)

