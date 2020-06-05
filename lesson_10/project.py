# ___________________________________________________________________ 72
from tkinter import Tk, Entry, Label, Button
from tkinter import Frame, LabelFrame, Listbox, StringVar
# from time import strftime  # import time
import time
from random import randint
from json import loads, dump


class Block:
    def __init__(self, root):

        root.geometry("450x300+300+200")
        root.resizable(False, False)
        root.title("Key speed")

# ___________Global__________________________________________________ 72
        # ошибок
        self.check_int = 0
        self.check_str = StringVar()
        self.check_str.set(None)

        # кол-во backspace
        self.repair_str = StringVar()
        self.repair_str.set(None)
        self.repair_int = 0
        # time
        self.time_start = float()
        self.ans_time = float()
        self.ans_time_str = StringVar()
        self.ans_time_str.set(None)



        # вывод текста
        self.txt_var = StringVar()
        self.txt_var_str = str()
        self.txt_var.set(
            'Put the cursor on the input field.'  +
            'After clicking start,' + 
            'the text will be here and the time report will start.' +
            'Сlicking  Enter to complete text entry.' +
            'Enter the name to save the result.'
        )
        
# ________________CREATE_____________________________________________ 72
        # Label = create
        frame_list = LabelFrame(root, text='Text')
        self.l_text = Label(
            frame_list,
            textvariable=self.txt_var,
            font='Arial 10',
            wraplength='80m'
        )
        self.l_error = Label(
            frame_list,
            textvariable=self.repair_str,
            font='Arial 13'
        )
        # entry = create
        self.e_input = Entry(frame_list, width=55)

        # button = create
        frame_butt = Frame(root)
        self.b_start = Button(
            frame_butt, command=self.start, text='Start'
        )  # 1 — запуск игры,
        self.b_look_hist = Button(
            frame_butt, command=self.history_look, text='History'
        )  # 2 — просмотр истории игр.
        self.b_clear = Button(
            frame_butt,
            command=self.clear,
            text='Clear'
        )  # Clear Global variable
        
        # Result
        grop_ans = LabelFrame(root, text='Result')
        self.ent_name = Entry(grop_ans, width=20)
        self.labl_ans_time = Label(grop_ans, textvariable=self.ans_time_str)
        self.labl_check = Label(grop_ans, textvariable=self.check_str)
        self.labl_repair = Label(grop_ans, textvariable=self.repair_str)
        self.b_save = Button(root, command=self.history_save, text='Save')


        # BIND
        self.e_input.bind("<BackSpace>", self.repair_text)
        self.e_input.bind("<Return>", self.check_input)
        
# _____________PACK__________________________________________________ 72
        # frame_list
        frame_list.pack(padx=3, pady=3)
        self.l_text.pack(padx=5, pady=5)
        self.l_error.pack(padx=3, pady=3, side='right')
        self.e_input.pack(padx=5, pady=5)
        
        # frame_button
        frame_butt.pack(padx=3, pady=3)
        self.b_start.pack(padx=5, pady=5, side='left')
        self.b_look_hist.pack(padx=5, pady=5, side='left')
        self.b_clear.pack(padx=5, pady=5, side='left')
        
        # grop_ans
        grop_ans.pack()
        Label(
            grop_ans,
            text='Name |    Word/time | Error | Repair',
            font='Arial 10'
        ).pack()
        self.ent_name.pack(padx=5, pady=5, side='left')
        self.labl_ans_time.pack(padx=5, pady=5, side='left')
        self.labl_check.pack(padx=5, pady=5, side='left')
        self.labl_repair.pack(padx=5, pady=5, side='left')
        self.b_save.pack(padx=5, pady=5)

    def start(self): # 1 — запуск игры
        text_r_data = list()
        with open(r"lesson_10\Data.txt", 'r', encoding='utf-8') as file:
            for i in file:
                text_r_data.append(i.strip())

            # random строка\вивод текста
            a = randint(0, len(text_r_data) - 1)
            self.txt_var_str = text_r_data[a]
            self.txt_var.set(text_r_data[a])
            self.print_speed_txt = len(text_r_data[a])

        self.buttn_time_start = time.time()

    def _check_size(self):  # нужен для 'def check_input()'
        # проверкаарка на розмер entry.get() and origin_text
        first = self.e_input.get().split()
        second = self.txt_var_str.split()
        a = len(first)
        b = len(second)
        if a > b:
            return filter
        else:
            return second

    def check_input(self, event):  # text check

        self.time_start = round((time.time() - self.buttn_time_start), 3)

        my_text = str(self.e_input.get()).split()
        origin_text = self.txt_var_str.split()
        # look who is bigger
        index = len(self._check_size())

        for word in range(index):  # длина списк (word)
            try:
                letter_word = self._check_size()
            except IndexError:
                try:
                    letter_word = my_text[word]
                except:
                    letter_word = origin_text[word]
            for letter in range(len(letter_word)):  # длина слова (letter)
                try:
                    if(my_text[word][letter] != origin_text[word][letter]):
                        self.check_int += 1
                except IndexError:
                    self.check_int += 1
        
        # Result check
        self.check_str.set(self.check_int)

        self.ans_time = round(((self.print_speed_txt / self.time_start) * 60), 0)
        self.ans_time_str.set(self.ans_time)

        print(f'\n {my_text} my,\n {origin_text} origin \n Error={self.check_int}')

    def history_save(self): # Sava result in json file
        if self.ent_name.get() == '':
            self.txt_var.set('"Enter the name to save the result."')
        else:
            with open(r'lesson_10\Bas_data.json', 'a', encoding='utf-8') as file:
                dump(
                    {
                        'Name': f'{self.ent_name.get()}',
                        'Print/Time': f'{self.ans_time}',
                        'Chek': f'{self.check_int}',
                        'Backspase': f'{self.repair_int}'
                    },
                    file
                )
                file.write('\n')
            self.clear()

    def clear(self):  # reset all variables
        self.check_int = 0
        self.repair_int = 0
        self.repair_str.set(None)
        self.time_start = float(0)
        self.txt_var.set(None)
        self.ans_time_str.set(None)
        self.check_str.set(None)
        

    def history_look(self):  # 2 — просмотр истории игр.
        cont = Tk()
        #cont.resizable(False, False)
        cont.title('Нistory')
        cont.geometry('500x400')

        self.l_box = Listbox(cont, width=60, height=20, font='Arial 10')
        self.l_box.pack(padx=5, pady=5)

        with open(r"lesson_10\Bas_data.json", 'r', encoding="utf-8") as file:
            for i in file:
                self.l_box.insert(0, i)

    def repair_text(self, event):  # += <backspase>
        self.repair_int += 1
        self.repair_str.set(f'{self.repair_int}')


root = Tk()
Block(root)

root.mainloop()
