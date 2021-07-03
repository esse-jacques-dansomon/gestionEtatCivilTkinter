from database import DataBase as db

class UserDao():
    def __init__(self, tableName='users', primaryKey='id'):
        self.tableName = tableName
        self.primaryKey = primaryKey

    def findAll(self):
        sql = "SELECT * FROM users"
        userDb = db.mycursor.cursor()
        userDb.execute(sql)
        users = userDb.fetchall()
        return users

    def insert(self, nom, prenom, login, password):
        sql = f"INSERT INTO {self.tableName} (nom, prenom, login, password) VALUES (%s, %s, %s , %s)"
        values=(nom, prenom, login, password)
        db.mycursor.cursor().execute(sql, values)
        db.persit()
        
    def loginAndPasswordExist(self, login, password):
        sql = "SELECT * FROM users WHERE login=%s AND password=%s"
        userDb = db.mycursor.cursor()
        value = (login, password)
        userDb.execute(sql, value)
        users = userDb.fetchone()
        return users

