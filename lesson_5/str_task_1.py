''' _________________________________________________________________ 72
1) Создать программу которая будет создавать копию самой себя. Копия
программы должна сохраняться рядом с исходной программой под
именем script_copy.
'''
def main():
    with open("lesson_5\\str_task_1.py", encoding= "utf-8") as r_text:
        with open("lesson_5\\copy_file.txt", 'w', encoding= "utf-8") as w_text:
                w_text.write(r_text.read())

main()