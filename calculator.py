from tkinter import *
from tkinter import messagebox

win = Tk()
# function define below
ooutput = StringVar()
g = ""


def val(num):

    global g
    g = g+str(num)

    ooutput.set(g)


def clr():

    global g
    g = ""
    ooutput.set(g)


def cal():
    global g
    cc = eval(g)
    g = str(cc)
    ooutput.set(cc)


win.title('Calculator')
win.geometry('350x350+600+200')
e1 = Entry(win, bg="pink",  justify='right', textvariable=ooutput,
           font=("Calibri", 20)).grid(rowspan=1, columnspan=100, ipadx=30, ipady=20)


bt1 = Button(win, text="7", command=lambda: val('7')).grid(
    row=1, column=0, ipadx=34, ipady=20)
bt2 = Button(win, text="8", command=lambda: val('8')).grid(
    row=1, column=1, ipadx=34, ipady=20)
bt3 = Button(win, text="9", command=lambda: val('9')).grid(
    row=1, column=2, ipadx=34, ipady=20)
bt4 = Button(win, text="x", command=lambda: val('*')).grid(
    row=1, column=3, ipadx=34, ipady=20)


bt5 = Button(win, text="4", command=lambda: val('4')).grid(
    row=2, column=0, ipadx=34, ipady=20)
bt6 = Button(win, text="5", command=lambda: val('5')).grid(
    row=2, column=1, ipadx=34, ipady=20)
bt7 = Button(win, text="6", command=lambda: val('6')).grid(
    row=2, column=2, ipadx=34, ipady=20)
bt8 = Button(win, text="-", command=lambda: val('-')
             ).grid(row=2, column=3, ipadx=34, ipady=20)


bt9 = Button(win, text="1", command=lambda: val('1')).grid(
    row=3, column=0, ipadx=34, ipady=20)
bt10 = Button(win, text="2", command=lambda: val('2')).grid(
    row=3, column=1, ipadx=34, ipady=20)
bt11 = Button(win, text="3", command=lambda: val('3')).grid(
    row=3, column=2, ipadx=34, ipady=20)
bt12 = Button(win, text="+", command=lambda: val('+')
              ).grid(row=3, column=3, ipadx=34, ipady=20)


bt9 = Button(win, text="0", command=lambda: val('0')).grid(
    row=4, column=0, ipadx=34, ipady=20)
bt10 = Button(win, text="%", command=lambda: val('/')).grid(
    row=4, column=1, ipadx=34, ipady=20)
bt11 = Button(win, text="c", command=lambda: clr()).grid(
    row=4, column=2, ipadx=34, ipady=20)
bt12 = Button(win, text="=", command=lambda: cal()).grid(
    row=4, column=3, ipadx=34, ipady=20)


win.mainloop()
