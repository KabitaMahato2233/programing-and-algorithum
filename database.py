from tkinter import*
import sqlite33
root=Tk()
root.title("Login")
f_name=Entry(root,width=30)
f_name.grid(row=0,colunm=1,padx=20)

l_name=Entry(root,width=30)
l_name=Entry(row=1,column=1)

Address=Entry(root,width=30)
Address.grid(row=1,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=3,column=1)


zipcode=Entry(root,width=30)
zipcode.grid(row=3,column=1)

f_name_label=Label(root,text="first Name")
f_name_label.grid(row=0,colunm=0)

l_name_label=Label(root,text="last name")
l_name_label.grid(row=1,column=0)

Address_label=Label(root,text="address")
Address_label.grid(row=2,column=0)

city_label=Label()(root,text="city")
city_label.grid(row=3,column=0)

state_label=Label(root,text="state")
state_label.grid(row=4,column=0)


#create textbox label


root.mainloop()