import pyodbc

def connect_acces():
    RUTA=r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\\SIS_VEN_MULTI_2010\\EMPRESAS_2010.mdb;'
    try:

        conn = pyodbc.connect(RUTA)
        return conn
        
    except Exception as e:
        #posible error
        print('Error: ',e)

    #finally:
        #cierra conexcion
        #conn.close()

def empresas():
        conn = connect_acces()
        query = "SELECT * FROM Empresas"
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data



