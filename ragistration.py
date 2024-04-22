from tkinter import *
from tkinter import ttk

# Now you can use ttk widgets and features

root = Tk()
root.geometry('700x700')
root.title('Registration Form')

#============title=================

Title = Label(root,text='Registration Form',font=('arial',17,'bold'))
Title.place(x=250,y=10)

#==============name=================

name = Label(root,text='Name : ',font=('arial',16,'bold'))
name.place(x=100,y=70)
e_name = Entry(root,text='Enter Name')
e_name.place(x=250,y=70,width=280,height=30)

#=============contact===============

contact = Label(root,text='Contact : ',font=('arial',16,'bold'))
contact.place(x=100,y=140)
e_contact = Entry(root,text='Enter Contact No')
e_contact.place(x=250,y=140,width=280,height=30)

#=============email===============

email = Label(root,text='Email : ',font=('arial',16,'bold'))
email.place(x=100,y=210)
e_email = Entry(root,text='Enter Your Email')
e_email.place(x=250,y=210,width=280,height=30)

#=============gender===============

gender=Label(root,text='Gender : ',font=('Arial',16,'bold'))
gender.place(x=100, y=280)
var=StringVar()     #==========>>>>>>>>>>   declare string variable for radiobutton
e_male=Radiobutton(root,text="Male",variable=var,value="male")
e_male.place(x=250,y=280)
e_female=Radiobutton(root,text="Female",variable=var,value="female")
e_female.place(x=350,y=280)

#=============city===============

city=Label(root,text='City : ',font=('Arial',16,'bold'))
select_option=StringVar()
city.place(x=100, y=350)
cities=['Ahemdabad','Surat','Anand','Rajkot','mumbai']
city_dropdown =ttk.Combobox(root, textvariable=select_option, values=cities)
city_dropdown.place(x=250,y=350,width=280,height=30)
select_option.set(cities[0])

#=================state==============

state=Label(root,text='State : ',font=('Arial',16,'bold'))
select_option=StringVar()
state.place(x=100, y=420)
states=['Aandhrapradesh','Gujarat','Utterpradesh','Bihar','Maharastra']
state_dropdown =ttk.Combobox(root, textvariable=select_option, values=states)
state_dropdown.place(x=250,y=420,width=280,height=30)
select_option.set(states[0])

#==================ragister buttons=======================

insert = Button(root,text='Ragister',font=('arial',14,'bold'),bg='yellow')
insert.place(x=250,y=490,width=200,height=50)

     #==========>>>>>>>>>>   declare string variable for Optionmenu
# e_city=OptionMenu(root,)
# mobile = Label(root,text='Mobile',font=('arial',12,'bold'))
# mobile.place(x=50,y=220)
# e_mobile = Entry(root,text='Enter mobile number',bg='yellow',fg='white')
# e_mobile.place(x=150,y=220)
# email = Label(root,text='email',font=('arial',12,'bold'))
# email.place(x=50,y=270)
# e_email = Entry(root,text='Enter email ',bg='yellow',fg='white')
# e_email.place(x=150,y=270)

#=========================== crud operation buttons ===========================

# insert = Button(root,text='insert',font=('arial',14,'bold'),bg='red')
# insert.place(x=50,y=350)
# update = Button(root,text='update',font=('arial',14,'bold'),bg='red')
# update.place(x=150,y=350)
# delete = Button(root,text='delete',font=('arial',14,'bold'),bg='red')
# delete.place(x=260,y=350)

root.mainloop()