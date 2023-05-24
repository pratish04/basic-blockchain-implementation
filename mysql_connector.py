import mysql.connector

def establish_connection():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pratish@Mysql04",
        database="blockchain_project"
    )
    print(cnx)
    return cnx

def close_connection(cnx):
    cnx.close()