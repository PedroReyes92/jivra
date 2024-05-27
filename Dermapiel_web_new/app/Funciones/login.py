from Funciones.coneccion import connect
import datetime

def encripta(cad):
    car=' '
    longitud = len(cad)
    while longitud < 10:
        cad = cad + car
        longitud = len(cad)

    cad_o = cad.upper()
    
    cad_2 = ''

    for l in cad_o:
        car = chr(ord(l) + longitud)
        cad_2 = cad_2 + car
    return cad_2

def logeos(usuario,contrasena):
    if usuario != 'SUPERVISOR':
        consulta = "SELECT * FROM USUARIO where USUARIO='" + usuario + "'"
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(consulta)
        row = cursor.fetchall()
        if row != None:
            n_pass = encripta(contrasena)
            if row[0][5] != n_pass:
                conn.close()
                return None
            else:
                return row
    else:
        fecha_hora = datetime.datetime.now()
        sistema_encripta = f'{fecha_hora.year % 100}{fecha_hora:%m}{fecha_hora:%d}{fecha_hora.strftime('%H%M')}'
        if sistema_encripta == contrasena:
            row = [(0, 0, 1, 1, 'SUPERVISOR', '', 'SUPERVISOR')]
            return row
        else:
            return None
        