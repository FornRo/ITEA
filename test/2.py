from tkinter import Tk, Toplevel, Button, Label, Entry, Text


root = Tk()

tl = Toplevel(root)
tl.title('1234')

# txt = Text(height=256, width=256)

entry = Entry(width=255, show='*')
label = Label(text='write you name and klick to button')
button = Button(root,
                text='take me',
                fg='red',
                bg='cyan',
                width=150,
                heigh=5)

root.title('Itrea-lesson-7')
root.geometry('600x400')

label.pack()
button.pack()
entry.pack()
txt.pack()
root.mainloop()
