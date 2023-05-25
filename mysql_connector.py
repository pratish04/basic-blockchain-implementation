import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def establish_connection():
    cnx = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )
    print(cnx)
    return cnx

def close_connection(cnx):
    cnx.close()