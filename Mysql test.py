import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="world"
)
mycursor = mydb.cursor()


sql = "INSERT INTO river (Upe, atkal upe) VALUES (%s, %s)"
val = [("Daugava", "Gauja"),
       ("Venta","Irbe")
]
       
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")