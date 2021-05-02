import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="pintu", database="pymysql")

mycursor = mydb.cursor()

# mycursor.execute("create table employee(Name varchar(200), Salary int(10))")

mycursor.execute("show tables")

for tb in mycursor:
    print(tb)