from Funciones.conec_acces import connect_acces


def empresas():
        conn = connect_acces()
        query = "SELECT * FROM Empresas"
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
