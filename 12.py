'''from tkinter import*
root=Tk()

def click():
    text1="Address: "+mytext.get("1.0",END)
    lbl.config(text=str(text1))

mytext=Text(root,font=20,width=20,height=10)
mytext.place(x=0,y=50)

btn= Button(root,text="Click Me",font=30,command=click)
btn.place(x=400,y=300)

lbl=Label(root,text="",font=30)
lbl.place(x=200,y=300)

root.mainloop()

#login window 
from tkinter import*
app=Tk()
usernamelabel=Label(text="username")
passwordlabel=Label(text="password")
userentry=Entry()
passentry=Entry()
usernamelabel.grid(row=1,column=1,padx=5,pady=5)
userentry.grid(row=1,column=2,padx=5,pady=5)

passwordlabel.grid(row=2,column=1,padx=5,pady=5)
passentry.grid(row=2,column=2,padx=5,pady=5)

btn=Button(text="login")
btn.grid(row=3,column=1,padx=10,pady=5)
app.mainloop()'''

