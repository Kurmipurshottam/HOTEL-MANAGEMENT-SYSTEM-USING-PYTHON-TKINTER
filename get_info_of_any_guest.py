from tkinter import *
import pymysql
from tkinter import messagebox as msg

mydb = pymysql.connect(host="localhost", user="root", password="", database="hotel_management_system")
mycursor = mydb.cursor()

def get_info_of_any_guest():
    root = Tk()
    root.geometry("1000x550")
    root.title("HOTEL MANAGEMENT SYSTEM")
    root.resizable(False, False)

    # Frame to contain the title
    frame1 = Frame(root, padx=85, pady=10, highlightbackground="black", highlightthickness=1)
    frame1.pack(pady=5)
    C1 = Label(frame1, text="YOU CLICKED ON  :  GET INFO OF GUEST", font=('Copperplate', 30, 'bold'))
    C1.pack()
    
    # frame2 = Frame(root, padx=432, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    # frame2.place(relx=0.0033,rely=0.50,relheight=0.5,relwidth=0.2,y=-31,h=15)
    # Label2 = Label(frame2,text="Names",font=('Copperplate', 100, 'bold'))
    # Label2.place(relx=0.0039, rely=0.54, height=10, width=10)

    frame2 = Frame(root, padx=90, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame2.place(relx=0.0084,rely=0.50,relheight=0.5,relwidth=0.12,y=-31,h=15)
    Label2 = Label(frame2,text="names",font=('Copperplate', 10, 'bold'))
    Label2.place(x=-65, y=0.0002, height=44, width=50)

    text1 = Text(frame2,font=('Copperplate', 10),background="#d9d9d9")
    text1.place(x=-80, y=63,width=90,height=200)

    frame3 = Frame(root, padx=90, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame3.place(relx=0.145,rely=0.50,relheight=0.5,relwidth=0.12,y=-31,h=15)
    Label2 = Label(frame3,text="address",font=('Copperplate', 10, 'bold'))
    Label2.place(x=-65, rely=0.0002, height=44, width=50)

    text2 = Text(frame3,font=('Copperplate', 10),background="#d9d9d9")
    text2.place(x=-80, y=63,width=90,height=200)

    frame4 = Frame(root, padx=90, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame4.place(relx=0.290,rely=0.50,relheight=0.5,relwidth=0.12,y=-31,h=15)
    Label2 = Label(frame4,text="mobile",font=('Copperplate', 10, 'bold'))
    Label2.place(x=-65, rely=0.0002, height=44, width=50)

    text3 = Text(frame4,font=('Copperplate', 10),background="#d9d9d9")
    text3.place(x=-80, y=63,width=90,height=200)

    frame5 = Frame(root, padx=90, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame5.place(relx=0.435,rely=0.50,relheight=0.5,relwidth=0.12,y=-31,h=15)
    Label2 = Label(frame5,text="day",font=('Copperplate', 10, 'bold'))
    Label2.place(x=-65, rely=0.0002, height=44, width=50)

    text4 = Text(frame5,font=('Copperplate', 10),background="#d9d9d9")
    text4.place(x=-80, y=63,width=90,height=200)

    frame6 = Frame(root, padx=90, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame6.place(relx=0.580,rely=0.50,relheight=0.5,relwidth=0.12,y=-31,h=15)
    Label2 = Label(frame6,text="type",font=('Copperplate', 10, 'bold'))
    Label2.place(x=-65, rely=0.0002, height=44, width=50)

    text5 = Text(frame6,font=('Copperplate', 10),background="#d9d9d9")
    text5.place(x=-80, y=63,width=90,height=200)

    frame7 = Frame(root, padx=90, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame7.place(relx=0.725,rely=0.50,relheight=0.5,relwidth=0.12,y=-31,h=15)
    Label2 = Label(frame7,text="r_no",font=('Copperplate', 10, 'bold'))
    Label2.place(x=-65, rely=0.0002, height=44, width=50)

    text6 = Text(frame7,font=('Copperplate', 10),background="#d9d9d9")
    text6.place(x=-80, y=63,width=90,height=200)

    frame8 = Frame(root, padx=90, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame8.place(relx=0.870,rely=0.50,relheight=0.5,relwidth=0.12,y=-31,h=15)
    Label2 = Label(frame8,text="pyment",font=('Copperplate', 10, 'bold'))
    Label2.place(x=-65, rely=0.0002, height=44, width=52)

    text7 = Text(frame8,font=('Copperplate', 10),background="#d9d9d9")
    text7.place(x=-80, y=63,width=90,height=200)

    # frame8 = Frame(root, padx=432, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    # frame8.place(relx=0.0033,rely=0.21,relheight=0.81,relwidth=0.495,y=-31,h=15)
    # Label2 = Label(frame8,text="Customer Names",font=('Copperplate', 20, 'bold'),background="#d9d9d9")
    # Label2.place(relx=0.83, rely=0.02, height=44, width=252)


    room = Label(root, text="ENTER THE ROOM NO", font=('Copperplate', 20, 'bold'))
    room.place(x=100, y=125)
    p_room = Label(root, text=":-", font=('Copperplate', 20, 'bold'))
    p_room.place(x=410, y=125)
    e_room = Entry(root, text="ENTER YOUR ROOM", bg='#d9d9d9')
    e_room.place(x=445, y=130, width=50, height=30)

    def submit_btn():
        room_no=int(e_room.get())
        room_no=int(e_room.get())
        query1="select * from guest where room_no = '%s' "
        args1=(room_no)
        c_room=mycursor.execute(query1,args1)
        if c_room!=0:
            query="select * from guest where room_no = '%s' "
            args=(room_no)
            mycursor.execute(query,args)
            data=mycursor.fetchone()
            print(len(data))
            for i in range(0,len(data)):
                print(data[6])
                p_name=data[0]
                p_address=data[1]
                p_mobile=str(data[2])
                p_day=str(data[3])
                p_roomtype=data[4]
                p_room=str(data[5])
                p_payment=data[6]
            text1.insert(INSERT,p_name+"\n")
            text2.insert(INSERT,p_address+"\n")
            text3.insert(INSERT,p_mobile+"\n")
            text4.insert(INSERT,p_day+"\n")
            text5.insert(INSERT,p_roomtype+"\n")
            text6.insert(INSERT,p_room+"\n")
            text7.insert(INSERT,p_payment+"\n")
            print(data)
            mydb.commit()
            msg.showinfo("Information Status", "Information Matched Successfully")
        else:
            msg.showwarning("Information Status", "Enter Valid Room No!!!")
        

    b_room = Button(root, text="GET DATA", font=('Copperplate', 20, 'bold'), width=12, height=2, bg='#d9d9d9',command=submit_btn)
    b_room.place(x=540, y=100)

    root.mainloop()

get_info_of_any_guest()