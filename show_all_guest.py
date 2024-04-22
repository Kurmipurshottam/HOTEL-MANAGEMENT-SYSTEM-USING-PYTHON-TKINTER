from tkinter import *
import pymysql
from tkinter import messagebox as msg

mydb = pymysql.connect(host="localhost", user="root", password="", database="hotel_management_system")
mycursor = mydb.cursor()

def show_all():
    root = Tk()
    root.geometry("1000x550")
    root.title("HOTEL MANAGEMENT SYSTEM")
    root.resizable(False, False)


    frame1 = Frame(root, padx=100, pady=10, highlightbackground="black", highlightthickness=1,background="#d9d9d9")
    frame1.pack(pady=5)
    C1 = Label(frame1, text="YOU CLICKED ON  :  SHOW GUEST LIST ", font=('Copperplate', 30, 'bold'),background="#d9d9d9")
    C1.pack()
        
    frame2 = Frame(root, padx=432, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame2.place(relx=0.0033,rely=0.21,relheight=0.81,relwidth=0.495,y=-31,h=15)
    Label2 = Label(frame2,text="Customer Names",font=('Copperplate', 20, 'bold'),background="#d9d9d9")
    Label2.place(relx=0.83, rely=0.02, height=44, width=252)

    frame3 = Frame(root, padx=432, pady=10, highlightbackground="black", highlightthickness=1,borderwidth="2",background="#d9d9d9")
    frame3.place(relx=0.51, rely=0.21, relheight=0.81, relwidth=0.485,y=-31, h=15)
    Label3 = Label(frame3,text="Room No",font=('Copperplate', 20, 'bold'),background="#d9d9d9")
    Label3.place(relx=0.70, rely=0.02, height=44, width=152)
 
    text1 = Text(frame2,font=('Copperplate', 15),background="#d9d9d9")
    text1.place(relx=0.79, rely=0.15,width=160,height=370)
    text2 = Text(frame3,font=('Copperplate', 15),background="#d9d9d9")
    text2.place(relx=0.66,rely=0.15,width=160,height=370)

    def submit_btn():
        query="select name,room_no from guest "
        mycursor.execute(query)
        details=mycursor.fetchall()
        print(details)
        print(len(details))
        for i in range(0,len(details)):
            i_name=details[i]
            p_name=i_name[0]
            p_room=str(i_name[1])
            print("p_name = ",p_name)
            print("p_room = ",p_room)
            text1.insert(INSERT,p_name+"\n")
            text2.insert(INSERT,p_room+"\n")

        mydb.commit()

    submit_btn()
    root.mainloop()

#show_all()