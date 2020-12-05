import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="25Szarfa"

)

cursor = db.cursor()

cursor.execute("create DATABASE datarepresentation")
