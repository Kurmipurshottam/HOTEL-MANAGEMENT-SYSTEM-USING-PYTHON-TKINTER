import pymysql
mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists hotel_management_system")
mydb = pymysql.connect(host="localhost",user="root",password="",database="hotel_management_system")
mycursor=mydb.cursor()
mycursor.execute("create table if not exists guest(name varchar(20),address varchar(20),mobile_no BIGINT,days int,room_type varchar(20),room_no int,pyment_method varchar(30) )")
mydb.commit()