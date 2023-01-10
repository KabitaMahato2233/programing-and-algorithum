# '''from tkinter import*
# win=Tk()#creating main id
# win.title("login")
# win.mainloop()#to open ui




# from tkinter import*
# win=Tk()#creating main id
# win.title("system".center(110))
# win.iconbitmap('a.ico.ico')#to open ui

# a=win.photoimage(files=' ')
# win=iconphoto(false,a)
# space='  '
# win.title(80*space+'system')'''

# from tkinter import*

# from tkinter import*
# win=Tk()#creating main id
# win.title("system".center(110))
# win.mainloop()#to open ui'
# from tkinter import*
# win=Tk()
# win.title('system')
# win.iconbitmap('a.ico.ico')
# win.maxsize(width=300,height=200)
# win.minsize(width=300,height=200)
# win.mainloop()
# win=Button(root,text="left",fg="green")
# win.pack(side=LEFT)

# from tkinter import*
# top=Tk()
# top.geometry("400x250")
# name=Label(top,text="Name").place(x=30,y=50)
# address=Label(top,text="Address").place(x=30,y=90)
# contact=Label(top,text="Contact").place(x=30,y=130)
# e1=Entry(top).place(x=80,y=50)
# e2=Entry(top).place(x=80,y=90)
# e3=Entry(top).place(x=95,y=130)
# top.mainloop()

# from tkinter import *

# import os

# from tkinter import messagebox




# def register_user():
#     Firstname_info=Firstname.get()
#     Lastname_info=Lastname.get()
#     Username_info=Username.get()
#     Email_info=Email.get()
#     Password_info=Password.get()
#     Button(register_screen,text="Register",height=2,width=15,command=register_screen).pack()
#     file=open(Firstname_info, "w")
#     file.write(Firstname_info + "\n")
#     file.write(Lastname_info + "\n")
#     file.write(Username_info + "\n")
#     file.write(Email_info + "\n")
#     file.write(Password_info)
#     file.close()
#     Firstname_info.delete(0,END)
#     Lastname_info.delete(0,END)
#     Username_info.delete(0,END)
#     Email_info.delete(0, END)
#     Password_info.delete(0, END)
#     Label(register_screen, text="Registration Success", fg="green").pack()
# def verify():
#     Email1 =Email_verify.get()
#     Password1 = Password_verify.get()
#     Email_login_entry.delete(0, END)
#     Password_login_entry.delete(0, END)
#     list_of_files = os.listdir()
#     if Email1 in list_of_files:
#         file1 = open(Email1, "r")
#         verify = file1.read().splitlines()
#         if Password1 in verify:
#             login_sucess()
#         else:
#             password_not_recognised()
# #     else:
#         Email_not_found()
# # Designing window for login
# def login():
#     global login_screen
#     login_screen = Toplevel(main_screen)
#     login_screen.title("Login")
#     login_screen.geometry("300x250")
#     Label(login_screen, text="Please enter details below to login").pack()
#     Label(login_screen, text="").pack()
#     global Firstname_verify
#     global Lastname_verify
#     global Username_verify
#     global Email_verify
#     global Password_verify
#     Email_verify = StringVar()
#     Password_verify = StringVar()
#     global Email_login_entry
#     global Password_login_entry
#     Label(login_screen, text="Email").pack()
#     Email_login_entry = Entry(login_screen, textvariable=Email_verify)
#     Email_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Label(login_screen, text="Password ").pack()
#     Password_login_entry = Entry(login_screen, textvariable=Password_verify, show= '*')
#     Password_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Button(login_screen, text="Login", width=10, height=1, command = verify).pack()
# def register():
#     global register_screen
#     register_screen=Toplevel(main_screen)
#     register_screen.title("Register")
#     register_screen.geometry("300x250")
#     global Firstname
#     global Lastname
#     global Username
#     global Email
#     global Password
#     global Firtsname_entry
#     global Lastname_entry
#     global Username_entry
#     global Email_entry
#     global Password_entry
#     Firtsname=StringVar()
#     Lastname=StringVar()
#     Username = StringVar()
#     Email=StringVar()
#     Password = StringVar()
#     Label(register_screen, text="Please enter details below", bg="Grey").pack()
#     Label(register_screen, text="").pack()
#     lable1 = Label(register_screen, text="Firstname ")
#     lable1.pack()
#     Firstname_entry = Entry(register_screen, textvariable=Lastname)
#     Firstname_entry.pack()
#     lable2 = Label(register_screen, text="Lastname ")
#     lable2.pack()
#     Lastname_entry = Entry(register_screen, textvariable=Lastname)
#     Lastname_entry.pack()
#     lable3 = Label(register_screen, text="Username  ")
#     lable3.pack()
#     Username_entry = Entry(register_screen, textvariable=Username)
#     Username_entry.pack()
#     lable4 = Label(register_screen, text="Email ")
#     lable4.pack()
#     Email_entry = Entry(register_screen, textvariable=Email)
#     Email_entry.pack()
#     lable5 = Label(register_screen, text="Password ")
#     lable5.pack()
#     Password_entry = Entry(register_screen, textvariable=Password, show='*')
#     Password_entry.pack()
#     Label(register_screen, text="").pack()
#     Button(register_screen, text="Register", width=10, height=1, bg="Grey", command = register_user).pack()
# def login_verify():
#     Email1 =Email_verify.get()
#     Password1 = Password_verify.get()
#     Email_login_entry.delete(0, END)
#     Password_login_entry.delete(0, END)
#     list_of_files = os.listdir()
#     if Email1 in list_of_files:
#         file1 = open(Email1, "r")
#         verify = file1.read().splitlines()
#         if Password1 in verify:
#             login_sucess()
#         else:
#             password_not_recognised()
#     else:
#         Email_not_found()
# # Designing popup for login success
# def login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(login_screen)
#     login_success_screen.title("Success")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Login Success").pack()
#     Button(login_success_screen, text="OK", command=delete_login_success).pack()
# # Designing popup for login invalid password
# def password_not_recognised():
#     global password_not_recog_screen
#     password_not_recog_screen = Toplevel(login_screen)
#     password_not_recog_screen.title("Success")
#     password_not_recog_screen.geometry("150x100")
#     Label(password_not_recog_screen, text="Invalid Password ").pack()
#     Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
# # Designing popup for Email not found
# def Email_not_found():
#     global Email_not_found_screen
#     Email_not_found_screen = Toplevel(login_screen)
#     Email_not_found_screen.title("Success")
#     Email_not_found_screen.geometry("150x100")
#     Label(Email_not_found_screen, text="Email Not Found").pack()
#     Button(Email_not_found_screen, text="OK", command=delete_Email_not_found_screen).pack()
# # Deleting popups
# def delete_login_success():
#     login_success_screen.destroy()
# def delete_password_not_recognised():
#     password_not_recog_screen.destroy()
# def delete_Email_not_found_screen():
#     Email_not_found_screen.destroy()
# # Designing Main(first) window
# def main_account_screen():
#     global main_screen
#     main_screen = Tk()
#     main_screen.geometry("300x250")
#     main_screen.title("Account Login")
#     main_screen.config(background="pink")
#     Label(text="Select Your Choice", bg="pink", width="300", height="2", font=("Calibri", 13)).pack()
#     Label(text="").pack()
#     Button(text="Login", height="2", width="30", command = login,bg='pink').pack()
#     Label(text="").pack()
#     Button(text="Register", height="2", width="30", command=register,bg='pink').pack()
#     main_screen.mainloop()
# main_account_screen()



'''from tkinter import*
window=Tk()
window.maxsize(width=300,height=300)
window.minsize(width=300,height=300)

def func():
    print("Button is clicked")
btn=Button(window,text="login",command=func)
btn.pack(side="top")
window.mainloop()

from tkinter import*
window=Tk()
def myClick():
    myLabel=Label(window,text="look! i clicked a button", fg='pink',bg="#00099",font=50)
    myLabel.pack()

my_button=Button(window,text="Click me",padx=10,pady=10,command=myClick,fg="pink",bg="blue")
my_button.pack()
window.mainloop()'''

# from tkinter import*
# window=Tk()
# def myClick():
#     myLabel=Label(window,text="look! i clicked a button", fg='pink',bg="#00099",font=50)
#     myLabel.pack()

# my_button=Button(window,text="Click me",padx=10,pady=10,command=myClick,fg="pink",bg="blue",state=DISABLED)
# my_button.pack()
# window.mainloop()

#Addition frames to program
# from tkinter import*
# window=Tk()
# frame=LabelFrame(window,text="this is my frame",padx=10,pady=10)
# frame.pack(padx=50,pady=50)
# b=Button(frame,text="dont click here")
# b2=Button(frame,text="....... here")
# b.grid(row=0,column=0)
# b2.grid(row=1,column=1)
# window.mainloop()

#radio button
# from tkinter import*
# window=Tk()
# def add():
#     print(var.get())
# var=IntVar()
# r1=Radiobutton(window,text="male", variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(window,text="female", variable=var,value=2,command=add)
# r2.pack(anchor=W)

# window.mainloop()

#config=chg value
# from tkinter import*
# window=Tk()
# def add():
#     selection="you have selected the option"+str(var.get())
#     label.config(text=selection)
# var=IntVar()
# r1=Radiobutton(window,text="option 1", variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(window,text="option 2", variable=var,value=2,command=add)
# r2.pack(anchor=W)
# r3=Radiobutton(window,text="option 3", variable=var,value=2,command=add)
# r3.pack(anchor=W)
# label=Label(window)
# label.pack()
# window.mainloop()

#check button -option select at many

# from tkinter import*
# # # import messageBox
# top=Tk()
# def add():
#     label.config(text=CheckVar1.get())
# CheckVar1=IntVar()

# C1=Checkbutton(top,text="music",variable=CheckVar1 , \
#                 onvalue=1, offvalue=0,height=5, \
#                     width=20)

# C1.pack()
# btn=Button(top,text="Click",command=add)
# label=Label(top,text="")
# label.pack()
# btn.pack()

# top.mainloop()

# from tkinter import*
# from PIL import Image,ImageTk
# window=Tk()
# window.title("login")
# #define img
# my_image=Image.open("nature.jpg")
# d=my_image.resize((400,400))
# c=ImageTk.PhotoImage(d)
# #create a label
# my_label=Label(image=c)
# my_label.pack()

# #Button quit option
# button_quit=Button(window,text="Exit", command=window.quit,width=20)
# button_quit.pack()
# # window.mainloop()


# from tkinter import *
# from PIL import ImageTk,Image
# from tkinter import messagebox

# root=Tk()
# root.title('Message Box')
# # root.iconbitmap('E:/image/global.ico')

# def popup():
#     #showunfo messagebox
#     messagebox.showinfo("this is my popup", "Hello World!")

# Button(root,text="Popup",command=popup).pack()

# mainloop()

#creat new window
# from tkinter import*
# from PIL import Image, ImageTk
# root=Tk()
# def open():
#     global my_img
#     top=Toplevel()
#     my_img=ImageTk.PhotoImage(Image.open("nature.jpg"))
#     my_label=Label(top,image=my_img)
#     my_label.pack(pady=10)
#     btn=Button(top,text="Close Window",command=top.destroy())
#     btn.pack()
# btnn=Button(root, text="open", command=open)
# btnn.pack()
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.geometry("200x200")
# def show():
#     label.config(text=clicked.get())
# #dropdown menu option
# options=[
#     "monday",
#     "tuesday",
#     "wednesday",
#     "thrusday",
#     "friday",
#     "saturday",
#     "sunday",
#     "sunday"
# ]
# clicked=StringVar()
# clicked.set("monday")

# drop=OptionMenu( root , clicked, *options)
# drop.pack()

# button=Button(root,text="click Me", command=show).pack()

# label=Label(root, text=" ")
# label.pack()
# root.mainloop()

from _ast import Lambda
from tkinter import*
root=Tk()

#defining title of project
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number =e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_number))

#definig the buttons
button_1=Button(root, text="1", padx=40, pady=20,command=lambda: button_click(1))
button_2=Button(root, text="2", padx=40, pady=20,command=lambda: button_click(2))
button_3=Button(root, text="3", padx=40, pady=20,command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=20,command=lambda: button_click(4))
button_5=Button(root, text="5", padx=40, pady=20,command=lambda: button_click(5))
button_6=Button(root, text="6", padx=40, pady=20,command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=20,command=lambda: button_click(7))
button_8=Button(root, text="8", padx=40, pady=20,command=lambda: button_click(8))
button_9=Button(root, text="9", padx=40, pady=20,command=lambda: button_click(9))
button_0=Button(root, text="0", padx=40, pady=20,command=lambda: button_click(0))
button_add=Button(root, text="+", padx=39, pady=20,command=button_add)
button_equal=Button(root, text="=", padx=91, pady=20,command=button_equal)
button_clear=Button(root, text="clear", padx=79, pady=20,command=button_clear)

#putting buttons on scren
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1 ,columnspan=2)

root.mainloop()





from _ast import Lambda
from tkinter import*
root=Tk()

#defining title of project
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))

def button_clear():
    e.delete(0,END)

def button_multi():
    first_number =e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num * int(second_number))

#definig the buttons
button_1=Button(root, text="1", padx=40, pady=20,command=lambda: button_click(1))
button_2=Button(root, text="2", padx=40, pady=20,command=lambda: button_click(2))
button_3=Button(root, text="3", padx=40, pady=20,command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=20,command=lambda: button_click(4))
button_5=Button(root, text="5", padx=40, pady=20,command=lambda: button_click(5))
button_6=Button(root, text="6", padx=40, pady=20,command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=20,command=lambda: button_click(7))
button_8=Button(root, text="8", padx=40, pady=20,command=lambda: button_click(8))
button_9=Button(root, text="9", padx=40, pady=20,command=lambda: button_click(9))
button_0=Button(root, text="0", padx=40, pady=20,command=lambda: button_click(0))
button_multi=Button(root, text="*", padx=39, pady=20,command=button_multi)
button_equal=Button(root, text="=", padx=91, pady=20,command=button_equal)
button_clear=Button(root, text="clear", padx=79, pady=20,command=button_clear)

#putting buttons on scren
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)
button_multi.grid(row=5,column=0)
button_equal.grid(row=5,column=1 ,columnspan=2)

root.mainloop()


from _ast import Lambda
from tkinter import*
root=Tk()

#defining title of project
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))

def button_clear():
    e.delete(0,END)

def button_division():
    first_number =e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num / int(second_number))

#definig the buttons
button_1=Button(root, text="1", padx=40, pady=20,command=lambda: button_click(1))
button_2=Button(root, text="2", padx=40, pady=20,command=lambda: button_click(2))
button_3=Button(root, text="3", padx=40, pady=20,command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=20,command=lambda: button_click(4))
button_5=Button(root, text="5", padx=40, pady=20,command=lambda: button_click(5))
button_6=Button(root, text="6", padx=40, pady=20,command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=20,command=lambda: button_click(7))
button_8=Button(root, text="8", padx=40, pady=20,command=lambda: button_click(8))
button_9=Button(root, text="9", padx=40, pady=20,command=lambda: button_click(9))
button_0=Button(root, text="0", padx=40, pady=20,command=lambda: button_click(0))
button_division=Button(root, text="/", padx=39, pady=20,command=button_division)
button_equal=Button(root, text="=", padx=91, pady=20,command=button_equal)
button_clear=Button(root, text="clear", padx=79, pady=20,command=button_clear)

#putting buttons on scren
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)
button_division.grid(row=5,column=0)
button_equal.grid(row=5,column=1 ,columnspan=2)

root.mainloop()