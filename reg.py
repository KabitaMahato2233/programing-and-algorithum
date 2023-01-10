'''from tkinter import*
window=Tk()
e=Entry(window,width=50,bg="blue",fg="white",borderwidth=5,font=20)
e.pack()

def myClick():
    myLabel=Label(window,text='hello'+ e.get())
    myLabel.pack()
btn=Button(window,text="Click me",padx=10,pady=10,command=myClick)
btn.pack()
window.mainloop()

from tkinter import*
window=Tk()
e=Entry(window,width=50,bg="blue",fg="white",borderwidth=5,font=20)
e.pack()

def myClick():
    myLabel=Label(window,text='hello'+ e.get())
    myLabel.pack()
    e.delete(0,END)
btn=Button(window,text="Click me",padx=10,pady=10,command=myClick)
btn.pack()
window.mainloop()

from tkinter import*
root=Tk()
root.title("GUI")
root.maxsize(width=600,height=600)
root.minsize(width=600,height=600)
#function
def add():
     x=var.get()
     print(x)
     mylabel1.config(text=x,bg="green")

#label1
mylabel=Label(root,text="User Name",fg="red",bg="yellow")
mylabel.place(x=10,y=10)
#label2
mylabel1=Label(root,text="Nothing",fg="red",bg="yellow")
mylabel.place(x=40,y=120)

#entry
var=StringVar()
ent=Entry(root,bg='black',fg="white",textvariable=var)
ent.place(x=80,y=10)

#button
btn=Button(root,text="submit",bg="green",fg="white",command=add)
btn.place(x=20,y=80)
root.mainloop()'''

#Bind
from tkinter import*
root=Tk()
root.title("GUI")
root.maxsize(width=600,height=600)
root.minsize(width=600,height=600)
#function
def add():
     x=var.get()
     print(x)
     mylabel1.config(text=x,bg="green")

#label1
mylabel=Label(root,text="User Name",fg="red",bg="yellow")
mylabel.place(x=10,y=10)
#label2
mylabel1=Label(root,text="Nothing",fg="red",bg="yellow")
mylabel.place(x=40,y=120)

#entry
var=StringVar()
ent=Entry(root,bg='black',fg="white",textvariable=var)
ent.place(x=80,y=10)

#button
btn=Button(root,text="submit",bg="green",fg="white",command=add)
btn.place(x=20,y=80)

#bind
btn=Button(root,text='Submit',bg="green",fg="white",command=add)
btn.place(x=70,y=60)
root.bind("<return>",lambda event:add())
root.mainloop()


