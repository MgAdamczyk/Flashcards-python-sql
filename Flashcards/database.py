import mysql.connector


def dbConnection():
    file = open("database_remotemysql.txt", "r")
    myHost = file.readline()
    myUser = file.readline()
    myPasswd = file.readline()[:10]
    myDatabase = file.readline()
    file.close()

    dataBase = mysql.connector.connect(
       host = myHost,
       user = myUser,
       passwd = myPasswd,
       database = myDatabase
    )
    return dataBase

