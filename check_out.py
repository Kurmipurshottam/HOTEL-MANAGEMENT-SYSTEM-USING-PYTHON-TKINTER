from tkinter import *
import pymysql
from tkinter import messagebox as msg

mydb = pymysql.connect(host="localhost", user="root", password="", database="hotel_management_system")
mycursor = mydb.cursor()

def checkout():
    root = Tk()
    root.geometry("1000x550")
    root.title("HOTEL MANAGEMENT SYSTEM")
    root.resizable(False, False)

    # Frame to contain the title
    frame1 = Frame(root, padx=100, pady=10, highlightbackground="black", highlightthickness=1)
    frame1.pack(pady=5)
    C1 = Label(frame1, text="YOU CLICKED ON      :          CHECK OUT ", font=('Copperplate', 30, 'bold'))
    C1.pack()
        
    room = Label(root, text="ENTER THE ROOM NO", font=('Copperplate', 20, 'bold'))
    room.place(x=250, y=130)
    p_room = Label(root, text=":-", font=('Copperplate', 20, 'bold'))
    p_room.place(x=560, y=130)
    e_room = Entry(root, text="ENTER YOUR room", bg='#d9d9d9')
    e_room.place(x=620, y=130, width=50, height=30)

    def submit_btn():
        room_no=int(e_room.get())
        query1="select * from guest where room_no = '%s' "
        args1=(room_no)
        c_room=mycursor.execute(query1,args1)
        print("========================",c_room)
        if c_room!=0:
            query="delete from guest where room_no ='%s'"
            args=(room_no)
            mycursor.execute(query , args)
            mydb.commit()

            msg.showinfo("Check-Out Status", "Check Out Successfully")
            
        else:
            msg.showwarning("Check-Out Status", "Enter Valid Room No!!")
        

    b_room = Button(root, text="CHECKOUT", font=('Copperplate', 20, 'bold'), width=12, height=2, bg='#d9d9d9',command=submit_btn)
    b_room.place(x=400, y=220)
    i_room = Label(root, text="THANKS FOR STAYE IN OUR HOTEL", font=('Copperplate', 20, 'bold'))
    i_room.place(x=250, y=370)
    i_room = Label(root, text="PLEASE VISIT AGAIN", font=('Copperplate', 20, 'bold'))
    i_room.place(x=350, y=430)
    root.mainloop()

# checkout()