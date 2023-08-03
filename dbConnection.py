import mysql.connector

db = mysql.connector.connect(
    host = "",
    user = "",
    passwd = ""
)

mycursor = db.cursor()