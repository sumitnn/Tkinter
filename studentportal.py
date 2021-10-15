
from tkinter import messagebox
from tkinter import *
import mysql.connector


win = Tk()


def log():

    if username.get() != '' and password.get() != "":

        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='tkinter')
        cursor = conn.cursor()
        try:
            sql = f"SELECT name, password FROM student WHERE name ='{username.get()}'  AND  password ='{password.get()}'  "

            cursor.execute(sql)
            res = cursor.fetchall()
            print(res)
            if res:

                messagebox.showinfo("LOGIN", "login Successfully")
                n = Toplevel(win)

                n.title("Registration Portal")
                n.geometry('650x650+200+400')
                n.configure(background="grey")

                Label(n, text=" WELCOME TO STUDENT PORTAL ", font=(
                    "Times", "28", "bold italic")).pack()
                username.set("")
                password.set("")

            else:
                messagebox.showerror(
                    " not found", "wrong password and username")

        except Exception as e:

            print(e)
            messagebox.showerror("Server Error", "Something Went Wrong")
        conn.close()

    else:
        messagebox.showerror("Blank Field", "Invalid error")


def new():

    def reg():

        if name.get() != '':
            conn = mysql.connector.connect(
                user='root', password='', host='127.0.0.1', database='tkinter')
            cursor = conn.cursor()
            sql = f"INSERT INTO `student`( `name`, `course`, `password`, `mobile`) VALUES('{name.get()}','{course.get()}','{password.get()}','{mobile.get()}')"
            try:

                cursor.execute(sql)
                conn.commit()

                messagebox.showinfo("Insert Data", "Successfully")

            except Exception as e:

                conn.rollback()
                print(e)
                messagebox.showerror("Server Error", "Something Went Wrong")
            conn.close()
            name.set("")
            course.set("")
            password.set("")
            mobile.set("")

        else:
            messagebox.showerror("Blank Field", "please enter values")

        pass
    name = StringVar()
    course = StringVar()
    password = StringVar()
    mobile = StringVar()
    new = Toplevel(win)
    new.title("Registration Portal")
    new.geometry('350x350+700+200')
    new.configure(background="grey")

    a = Label(new, text="User Name", font=(
        "Times", "18", "bold italic")).grid(row=0, column=0)
    b = Label(new, text="Course", font=(
        "Times", "18", "bold italic")).grid(row=1, column=0)
    c = Label(new, text="Password", font=(
        "Times", "18", "bold italic")).grid(row=2, column=0)
    d = Label(new, text="Contact Number", font=(
        "Times", "18", "bold italic")).grid(row=3, column=0)
    a1 = Entry(new, textvariable=name).grid(row=0, column=1)
    b1 = Entry(new, textvariable=course).grid(row=1, column=1)
    c1 = Entry(new, show="*", textvariable=password).grid(row=2, column=1)
    d1 = Entry(new, textvariable=mobile).grid(row=3, column=1)

    btn = Button(new, text="Submit", command=reg).grid(row=4, column=1)


win.title("Student Portal")

win.geometry('200x150+500+200')
# username label and text entry box
usernameLabel = Label(win, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(win, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(win, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(win, textvariable=password,
                      show='*').grid(row=1, column=1)

# validateLogin = partial(validateLogin, username, password)

# login button
loginButton = Button(win, text="Login", command=log).grid(row=5, column=0)
RegButton = Button(win, text="Register",
                   command=new).grid(row=5, column=1)


win.mainloop()
