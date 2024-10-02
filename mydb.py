import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Bach2308_.',

)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE diepbach")

print("All Done!")