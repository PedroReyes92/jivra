import mariadb
import sys

# Connect to MariaDB Platform
def connect():
    try:
        conn = mariadb.connect(
            user="Jivra_Pruebas",
            password="Jivra_2024",
            host="jivra.com.mx",
            port=3306,
            database="dermacutanea_pruebas")
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)







"""import pyodbc

def connect():
    SERVER = 'JIVRA-PRUEBAS'
    DATABASE = 'DERMAPIEL'
    USERNAME= 'sa'
    PASSWORD= 'Jivra_2023'

    try:

        conn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=Yes')
        return conn
        
    except Exception as e:
        #posible error
        print('Error: ',e)

    #finally:
        #cierra conexcion
        #conn.close()
"""