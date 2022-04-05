import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  database='db',
  user="yourusername",
  password="yourpassword"
)

cursor = db.cursor()
