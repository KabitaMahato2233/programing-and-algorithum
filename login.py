from tkinter import*
from tkinter import messagebox
import ast

window=Tk()
window.title('LOGIN')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

def signup():
    username=user.get()
    password=code.get()
    confirm_password=confirm.get()

    if password==confirm_password:
        try:
            file=open('datasheet.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo('Signup', 'Sucessfully signed up')

        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close()


logo=Frame(window,width=600,height=500,bg='#3cdfff')
logo.place(x=500,y=0)

frame=Frame(window,width=400, height=450, bg='#fff')
frame.place(x=50, y=35)

heading= Label(frame,text='Sign Up', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=150,y=3)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.input(0,'First Name')


user=Entry(frame,width=15, fg="black", border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=1,y=80)
user.insert(0,'First Name')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=175, height=2, bg='black').place(x=0,y=107)

def on_enter(e):
    user1.delete(0,'end')

def on_leave(e):
    name=user1.get()
    if name=='':
        user1.input(0,'Last Name')

user1=Entry(frame,width=15, fg="black", border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user1.place(x=200,y=80)
user1.insert(0,'Last Name')
user1.bind('<FocusIn>', on_enter)
user1.bind('<FocusOut>', on_leave)

Frame(frame, width=175, height=2, bg='black').place(x=200,y=107)

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.input(0,'Email')

code= Entry(frame,width=25, fg='black', border=0, bg= 'white', font=('Microsoft YaHei UI Light', 11))
code.place(x=1, y=150)
code.insert(0,'Email')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=0, y=177)

def on_enter(e):
    confirm.delete(0,'end')

def on_leave(e):
    name=confirm.get()
    if name=='':
        confirm.insert(0,'Confirm Password')

confirm= Entry(frame,width=25, fg='black', border=0, bg= 'white', font=('Microsoft YaHei UI Light', 11))
confirm.place(x=1, y=220)
confirm.insert(0,'Mobile Number')
confirm.bind('<FocusIn>', on_enter)
confirm.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=0, y=247)

Button(frame,width=39, pady=7, text='Sign Up', bg='#57a1f8',fg='white',border=0, command=signup). place(x=29, y=350)
label= Label(frame, text='I have an acoount', fg='Black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=90,y=400)

def on_enter(e):
    dob.delete(0,'end')

def on_leave(e):
    name=confirm.get()
    if name=='':
        dob.insert(0,'Date of Birth     DD/MM/YYYY')

dob = Entry(frame,width=25, fg='black', border=0, bg= 'white', font=('Microsoft YaHei UI Light', 11))
dob.place(x=1, y=290)
dob.insert(0,'Date of Birth     DD/MM/YYYY')
dob.bind('<FocusIn>', on_enter)
dob.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=0, y=315)

signin= Button(frame, width=6, text='Sign In',border=0, bg='white', cursor='hand2', fg='#57a1f8')
signin.place(x=200,y=400)

window.mainloop()