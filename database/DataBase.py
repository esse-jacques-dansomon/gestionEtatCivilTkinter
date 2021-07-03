import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="gestion_etat_civil"
)

mycursor = mydb

def persit():
    mydb.commit()


