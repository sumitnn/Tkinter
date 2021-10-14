# Tkinter With DataBase
from tkinter import *
import mysql.connector
from tkinter import messagebox

win = Tk()

name = StringVar()
course = StringVar()
email = StringVar()
gender = StringVar()


def clean():
    name.set('')
    email.set('')
    course.set('')
    gender.set('')


def database():
    if name.get() != '':
        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='tkinter')
        cursor = conn.cursor()
        sql = f"INSERT INTO `userdata`( `name`, `course`, `email`, `gender`) VALUES ('{name.get()}','{course.get()}','{email.get()}','{gender.get()}')"
        try:

            cursor.execute(sql)
            conn.commit()

            messagebox.showinfo("Insert Data", "Successfully")

        except Exception as e:

            conn.rollback()
            print(e)
            messagebox.showerror("Server Error", "Something Went Wrong")
        conn.close()
        clean()
    else:
        messagebox.showerror("Blank Field", "please enter values")


win.title("Tkinter With DataBase")
win.configure(background='pink')
win.geometry('400x500')
Label(win, text='Enter User Name').grid(row=0, column=0)
e1 = Entry(win, textvariable=name).grid(row=0, column=1)


Label(win, text='Enter Course').grid(row=1, column=0)
e2 = Entry(win, textvariable=course).grid(row=1, column=1)


Label(win, text='Enter Email').grid(row=2, column=0)
e3 = Entry(win, textvariable=email).grid(row=2, column=1)

R1 = Radiobutton(win, text="Male",  variable=gender, value='Male')
R1.grid(row=3, column=0)


R2 = Radiobutton(win, text="Female",  variable=gender, value='Female')
R2.grid(row=4, column=0)

B = Button(win, text="Create User", command=database,
           bg='yellow', activebackground='orange')
B.grid(row=5, column=1)

win.mainloop()
