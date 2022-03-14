from tkinter import *
import tkinter.messagebox as MessageBox
root= Tk()
root.title("Login Form")
root.geometry("800x300")
root.configure(bg="light blue")

def validate():
    username_result = t_uname.get()
    password_result = t_password.get()

    if username_result=="AYO" and password_result=="niitagbara":
        MessageBox.showinfo("Login Access","Login Successful")
    else:
         MessageBox.showinfo("Access Denied","Incorrect Credentials")

title = Label(root,text="Login Form",bg="light blue",font=("bold",13))
title.place(x=200,y=30)

uname = Label(root,text="Username",bg="light blue",font=("bold",13))
uname.place(x=100,y=80)
t_uname = Entry()
t_uname.place(x=200,y=80)
password = Label(root,text="password",bg="light blue",font=("bold",13))
password.place(x=100,y=110)
t_password = Entry(root,show="*")
t_password .place(x=200,y=110)

submit= Button(root,text="Login", fg="brown",bg="light blue", command = validate)
submit.place(x=200,y=160)

root.mainloop()