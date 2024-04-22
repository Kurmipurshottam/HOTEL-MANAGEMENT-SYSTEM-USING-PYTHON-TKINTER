from tkinter import *
import pymysql
from tkinter import messagebox as msg
import random

# Establishing connection with the MySQL database
mydb = pymysql.connect(host="localhost", user="root", password="", database="hotel_management_system")
mycursor = mydb.cursor()

# Function to handle the check-in process
def checkin():

    # Function to validate and process name entry
    def name_ok():
        if e_name.get() == "":
            msg.showinfo("Input Message", "Name Entered Fail")
        else:
            msg.showinfo("Input Message", "Name Inputed Successfully")

    # Function to validate and process address entry
    def address_ok():
        if e_address.get() == "":
            msg.showinfo("Input Message", "Address Entered Fail")
        else:
            msg.showinfo("Input Message", "Address Inputed Successfully")

    # Function to validate and process mobile number entry
    def mobile_ok():
        if e_number.get() == "":
            msg.showinfo("Input Message", "Mobile Number Entered Fail")
        else:
            msg.showinfo("Input Message", "Mobile Number Inputed Successfully")

    # Function to validate and process number of days entry
    def days_ok():
        if e_days.get() == "":
            msg.showinfo("Input Message", "Days Entered Fail")
        else:
            msg.showinfo("Input Message", "Days Inputed Successfully")

    # Main Check-in window
    root = Tk()
    root.geometry("1000x550")
    root.title("HOTEL MANAGEMENT SYSTEM")
    root.resizable(False, False)

    # Frame for title
    frame1 = Frame(root, padx=100, pady=10, highlightbackground="black", highlightthickness=1)
    frame1.pack(pady=5)
    C1 = Label(frame1, text="YOU CLICKED ON      :          CHECK IN ", font=('Copperplate', 30, 'bold'))
    C1.pack()

    # Name entry
    name = Label(root, text="ENTER YOUR NAME", font=('Copperplate', 15, 'bold'))
    name.place(x=50, y=123)
    m_name = Label(root, text=":", font=('Copperplate', 15, 'bold'))
    m_name.place(x=320, y=123)
    e_name = Entry(root, text="ENTER YOUR NAME", bg='#d9d9d9')
    e_name.place(x=450, y=120, width=350, height=30)
    b_name = Button(root, text="OK", font=('Copperplate', 10, 'bold'), width=3, height=1, bg='#d9d9d9', command=name_ok)
    b_name.place(x=870, y=120)

    # Address entry
    address = Label(root, text="ENTER YOUR ADDRESS", font=('Copperplate', 15, 'bold'))
    address.place(x=50, y=156)
    m_address = Label(root, text=":", font=('Copperplate', 15, 'bold'))
    m_address.place(x=320, y=156)
    e_address = Entry(root, text="ENTER YOUR ADDRESS", bg='#d9d9d9')
    e_address.place(x=450, y=153, width=350, height=30)
    b_address = Button(root, text="OK", font=('Copperplate', 10, 'bold'), width=3, height=1, bg='#d9d9d9', command=address_ok)
    b_address.place(x=870, y=153)

    # Mobile number entry
    number = Label(root, text="ENTER MOBILE NUMBER", font=('Copperplate', 15, 'bold'))
    number.place(x=50, y=189)
    m_number = Label(root, text=":", font=('Copperplate', 15, 'bold'))
    m_number.place(x=320, y=189)
    e_number = Entry(root, text="ENTER MOBILE NUMBER", bg='#d9d9d9')
    e_number.place(x=450, y=189, width=350, height=30)
    b_number = Button(root, text="OK", font=('Copperplate', 10, 'bold'), width=3, height=1, bg='#d9d9d9', command=mobile_ok)
    b_number.place(x=870, y=189)

    # Number of days entry
    days = Label(root, text="NUMBER OF DAYS", font=('Copperplate', 15, 'bold'))
    days.place(x=50, y=222)
    m_days = Label(root, text=":", font=('Copperplate', 15, 'bold'))
    m_days.place(x=320, y=222)
    e_days = Entry(root, text="NUMBER OF DAYS", bg='#d9d9d9')
    e_days.place(x=450, y=222, width=350, height=30)
    b_days = Button(root, text="OK", font=('Copperplate', 10, 'bold'), width=3, height=1, bg='#d9d9d9', command=days_ok)
    b_days.place(x=870, y=222)

    # Room selection
    rooms = Label(root, text="CHOOSE YOUR ROOM", font=('Copperplate', 15, 'bold'))
    rooms.place(x=230, y=280)

    # Function to handle submission
    def submit_btn():
        try:
            name = e_name.get()
            address = e_address.get()
            m_number = e_number.get()
            days = int(e_days.get())
            deluxe_r = ""
            general_r = ""
            fulld_r = ""
            joint_r = ""
            if d_var.get() == 1:
                deluxe_r = "Deluxe"
            if g_var.get() == 1:
                general_r = "General"
            if fd_var.get() == 1:
                fulld_r = "Full Deluxe"
            if j_var.get() == 1:
                joint_r = "Joint"
            room = deluxe_r + "" + general_r + "" + fulld_r + "" + joint_r
            pc_payment = ""
            dc_payment = ""
            if pc_var.get() == 1:
                pc_payment = "CASH"
            if dc_var.get() == 1:
                dc_payment = "CREDIT/DEBIT"
            pyment_all = pc_payment + "" + dc_payment
            deluxe_list = [1, 11, 21, 31, 41]
            genral_list = [2, 12, 22, 32, 42, 52, 55, ]
            fulld_list = [3, 13, 23, 33, 43, 53, 56, 67, 78]
            joint_list = [4, 14, 24, 34, 43, 53, 63, 67, 87, 98, 58, 5]
            room_no = ""
            if room == "Deluxe":
                room_no = int(random.choice(deluxe_list))
                deluxe_list.remove(room_no)
            elif room == "General":
                room_no = int(random.choice(genral_list))
                genral_list.remove(room_no)
            elif room == "Full Deluxe":
                room_no = int(random.choice(fulld_list))
                fulld_list.remove(room_no)
            elif room == "Joint":
                room_no = int(random.choice(joint_list))
                print(type(room_no))
                joint_list.remove(room_no)
            query = "insert into guest(name,address,mobile_no,days,room_type,room_no,pyment_method) values(%s,%s,%s,%s,%s,%s,%s)"
            args = (name, address, m_number, days, room, room_no, pyment_all)
            mycursor.execute(query, args)
            mydb.commit()
            
            msg.showinfo("Check-In Status", "Inputed Successfully")
        except Exception as e:
            msg.showerror("Error", f"An error occurred: {str(e)}")
        finally:

            pass


        print("@@@@@@@@@@@@@@@@@@@@@ Receipt @@@@@@@@@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@@ HOTEL MANAGEMENT SYSTEM @@@@@@@@@@@@@")
        print("Name: ", name)
        print("Address: ", address)
        print("Mobile No: ", m_number)
        print("Days: ", days)
        print("Room: ", room)
        print("Room No: ", room_no)
        bill = ""
        if room == "Deluxe":
            bill = int(1000 * days)
        elif room == "General":
            bill = int(500 * days)
        elif room == "Full Deluxe":
            bill = int(1500 * days)
        elif room == "Joint":
            bill = int(700 * days)
        print("Total Bill: ", bill)

        print(type(room))
        print(type(room_no))
        print(type(bill))

    # Room type selection variables
    d_var = IntVar()
    g_var = IntVar()
    fd_var = IntVar()
    j_var = IntVar()

    # Function to handle Deluxe room selection
    def deluxe_select():
        if d_var.get() == 1:
            g_var.set(0)
            fd_var.set(0)
            j_var.set(0)

    # Function to handle General room selection
    def general_select():
        if g_var.get() == 1:
            d_var.set(0)
            fd_var.set(0)
            j_var.set(0)

    # Function to handle Full Deluxe room selection
    def fulld_select():
        if fd_var.get() == 1:
            d_var.set(0)
            g_var.set(0)
            j_var.set(0)

    # Function to handle Joint room selection
    def joint_select():
        if j_var.get() == 1:
            d_var.set(0)
            g_var.set(0)
            fd_var.set(0)

    # Checkbuttons for room selection
    deluxe = Checkbutton(root, text="DELUXE", variable=d_var, font=('Copperplate', 15, 'bold'), command=deluxe_select)
    deluxe.place(x=50, y=320)

    general = Checkbutton(root, text="GENERAL", variable=g_var, font=('Copperplate', 15, 'bold'), command=general_select)
    general.place(x=520, y=320)

    F_deluxe = Checkbutton(root, text="FULL DELUEX", variable=fd_var, font=('Copperplate', 15, 'bold'), command=fulld_select)
    F_deluxe.place(x=50, y=360)

    joint = Checkbutton(root, text="JOINT", variable=j_var, font=('Copperplate', 15, 'bold'), command=joint_select)
    joint.place(x=520, y=360)

    # Payment selection
    pyment = Label(root, text="CHOOSE YOUR PAYMENT METHOD", font=('Copperplate', 15, 'bold'))
    pyment.place(x=180, y=418)

    # Payment variables
    pc_var = IntVar()
    dc_var = IntVar()

    # Function to handle cash payment selection
    def cash_select():
        if pc_var.get() == 1:
            dc_var.set(0)

    # Function to handle card payment selection
    def card_select():
        if dc_var.get() == 1:
            pc_var.set(0)

    # Checkbuttons for payment selection
    cash = Checkbutton(root, text="BY CASH", variable=pc_var, onvalue=1, offvalue=0, font=('Copperplate', 15, 'bold'), command=cash_select)
    cash.deselect()
    cash.place(x=50, y=460)

    card = Checkbutton(root, text="CREDIT/DEBIT CARD", height=2, variable=dc_var, font=('Copperplate', 15, 'bold'), onvalue=1, offvalue=0, command=card_select)
    card.deselect()
    card.place(x=520, y=460)

    # Submit button
    submit = Button(root, text="SUBMIT", font=('Copperplate', 20, 'bold'), width=10, height=3, bg='#d9d9d9', command=submit_btn)
    submit.place(x=730, y=340)

    root.mainloop()
    
# Calling the checkin function to start the application
checkin()



