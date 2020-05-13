''' _________________________________________________________________ 72
1) Создать программу которая будет создавать копию самой себя. Копия
программы должна сохраняться рядом с исходной программой под
именем script_copy.
'''
def main():
    with open("lesson_5\\str_task_1.py", encoding= "utf-8") as read_text:
        with open("lesson_5\\copy_file.txt", 'w', encoding= "utf-8") as write_text:
                write_text.write(read_text.read())

main()