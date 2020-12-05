import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="25Szarfa",
  database="datarepresentation"
)

cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Karolina",40)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)