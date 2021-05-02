import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="pintu", database="pymysql")

mycursor = mydb.cursor()

sql = "DELETE from employee  where name='Jung'"
mycursor.execute(sql)

mydb.commit()