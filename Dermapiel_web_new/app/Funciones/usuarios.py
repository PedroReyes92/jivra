from Funciones.coneccion import connect


def con_usuarios():
        conn = connect()
        query = "SELECT Id_Usuario,Usuario FROM Usuario"
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data


def farmacias():
        conn = connect()
        query = "SELECT Id_Farmacia,Descripcion FROM FARMACIAS"
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data