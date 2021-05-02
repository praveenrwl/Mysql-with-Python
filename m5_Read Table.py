import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="pintu", database="pymysql")

mycursor = mydb.cursor()

# mycursor.execute("Select name from employee")
mycursor.execute("Select * from employee")

# myresult = mycursor.fetchone()
myresult = mycursor.fetchall()

for row in myresult:
    print(row)