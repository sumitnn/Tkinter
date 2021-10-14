import random
from tkinter import *
import pyperclip


win = Tk()


def copy_password():
    pyperclip.copy(strPassword.get())


def create_password():
    characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*()[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
    res = "".join(random.sample((characters), k=lenPassword.get()))
    strPassword.set(res)


win.title("Random Password Generator")

win.geometry("450x220+500+300")


lblPassword = Label(
    win, text='Set Password Length', font='Ubuntu 15 bold')
lblPassword.pack()

lenPassword = IntVar()

length = Spinbox(win, from_=8, to_=16,
                 textvariable=lenPassword, width=4, font='Ubuntu 15 bold')
length.pack(pady=10)


lblmsg1 = Label(win, text='Generated Password', font='Ubuntu 12')
lblmsg1.pack()

strPassword = StringVar()

textData = Entry(win, textvariable=strPassword, width=15, font='Ubuntu 15')
textData.pack()


btnPassword = Button(
    win, text="Generate Password", command=create_password)
btnPassword.pack(padx=50, pady=5, side=LEFT)
btnCopy = Button(win, text='Copy', command=copy_password)
btnCopy.pack(side=LEFT)
win.mainloop()
