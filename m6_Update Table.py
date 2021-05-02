import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="pintu", database="pymysql")

mycursor = mydb.cursor()

sql = "update employee set salary=50000 where name='Jung'"
mycursor.execute(sql)

mydb.commit()