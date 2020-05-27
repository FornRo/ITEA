''' _________________________________________________________________ 72
    1) Создать приложение записной книги с помощью модуля Tkinter.
    Пользователь вводит следующую информацию о контакте:
    Имя, Фамилия, Номер телефона, Адрес.
    По нажатию на кнопку сохранить,новый контакт должен записываться в файл,
    так же должно сохраниться время создания контакта.
    При нажатии на кнопку «Мои контакты» выводить все доступные контакты (из
    файла) в новом окне. В новом окне создать кнопку («Очистить список»), при
    нажатии на которую файл с контактами будет очищаться и окно с контактами
    будет закрыто.
'''

from tkinter import Tk, Entry, Label, Button, Frame, LabelFrame, Listbox
from time import strftime  # import time


class Block:
    def __init__(self, root):

        root.geometry("250x240+300+200")
        root.resizable(False, False)
        root.title("Notebook")

        # Global str()
        self.name = str()
        self.surname = str()
        self.number = str()
        self.town = str()

        # input date = create LabelFrame \ Entry
        lf_name = LabelFrame(root, text='Имя')
        self.e_name = Entry(lf_name, width=30)
        lf_surname = LabelFrame(root, text='Фамилия')
        self.e_surname = Entry(lf_surname, width=30)
        lf_number = LabelFrame(root, text='Номер телефона')
        self.e_number = Entry(lf_number, width=20)
        lf_town = LabelFrame(root, text='Адрес')
        self.e_town = Entry(lf_town, width=30)

        # buttons = create LabelFrae \ Button
        lf_button = Frame(root)
        self.b_save = Button(
            lf_button, command=self.write_date, text='Cохранить')
        self.b_clear = Button(
            lf_button, comman=self.list_box, text='Мои контакты')

        # all pack
        lf_name.pack()
        self.e_name.pack(padx=3, pady=3)
        lf_surname.pack()
        self.e_surname.pack(padx=3, pady=3)
        lf_number.pack()
        self.e_number.pack(padx=3, pady=3)
        lf_town.pack()
        self.e_town.pack(padx=3, pady=3)
        lf_button.pack()
        self.b_save.pack(side='top')
        self.b_clear.pack(side='bottom')

    # create new window list_box
    def list_box(self):
        self.cont = Tk()
        self.cont.title('Мои контакты')
        self.cont.geometry('400x250')

        self.l_box = Listbox(self.cont, width=55, height=15)
        # read txt and input list_box
        with open(r"lesson_7\Bas_Ddate.txt", 'r', encoding="utf-8") as file:
            for i in file:
                self.l_box.insert(0, i)

        Button(self.cont, comman=self.clear_list,
               text='Очистить список',
               width=20).pack(side='right',
                              padx=3,
                              pady=3)
        self.l_box.pack(padx=3, pady=3)
        self.cont.mainloop()

    # clear file
    def clear_list(self):
        with open(r"lesson_7\Bas_Ddate.txt", 'w', encoding="utf-8") as file:
            file.write('')
        self.cont.destroy()

    # Def func save in file
    def write_date(self):
        with open(r"lesson_7\Bas_Ddate.txt", 'a', encoding="utf-8") as file:
            file.write(
                str(
                    strftime("%X") + ' >> ' +
                    self.e_name.get() + ', ' +
                    self.e_surname.get() + ', ' +
                    self.e_number.get() + ', ' +
                    self.e_town.get() + '\n'
                )
            )


# ______________
root = Tk()
Block(root)

root.mainloop()
