import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="pintu", database="pymysql")

mycursor = mydb.cursor()

sqlform = "insert into employee (Name, Salary) values (%s, %s)"

employee = [("Sung",35000),("Arhad", 45000),("Jung",55000)]

mycursor.executemany(sqlform, employee)

mydb.commit()