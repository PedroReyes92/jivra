from Funciones.coneccion import connect

class Medicamento:
    def todos(self):
        try:
            query = "select * from Medicamento"
            con = connect()
            cursor = con.cursor()
            cursor.execute(query)
            row =cursor.fetchall()
            #intento de diccionario
            insertObjeo = []
            columnames = [column[0] for column in cursor.description]
            for r in row:
                insertObjeo.append(dict(zip(columnames, r)))
            cursor.close()
            return insertObjeo
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e
    
    def total(self):
        try:
            query = "SELECT COUNT(*) AS Total FROM Medicamento"
            con = connect()
            cursor = con.cursor()
            cursor.execute(query)
            row =cursor.fetchall()
            for r in row:
                result= r
            return result
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def todospaginados(self, top, pagina):
        try:
            query = f"SELECT * FROM Medicamento ORDER BY Fecha_Ultimo_Movto DESC LIMIT {top} OFFSET {pagina}"
            con = connect()
            cursor = con.cursor()
            cursor.execute(query)
            row =cursor.fetchall()
            #intento de diccionario
            insertObjeo = []
            columnames = [column[0] for column in cursor.description]
            for r in row:
                insertObjeo.append(dict(zip(columnames, r)))
            cursor.close()
            return insertObjeo
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e
    
    def existe(self, id_ariculo):
        try:
            query= "select Id_Articulo from Medicamento where Id_Articulo='"+ id_ariculo +"'"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            if row:
                return True
            else:
                return False
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def grabar(self, ActualizacionAutomatica, CODIGO_BARRA, Costo_Promedio, Des_Abreviado, Descontinuado, Descripcion, Descuento, Exis_Maximo, Exis_Minimo, Existencia, Fecha, Id_Articulo, Id_Articulo_Datos, Id_Laboratorio, Id_Linea, Id_Presentacion, IVA, Precio_Venta, Promocionado, Servicio, Ultimo_Precio_Compra, CLAVEPRODSERV, OBJETOIMP):
        try:
            query= f"""INSERT INTO Medicamento (ActualizacionAutomatica, CODIGO_BARRA, Costo_Promedio, Des_Abreviado, Descontinuado, Descripcion, 
            Descuento, Exis_Maximo, Exis_Minimo, Existencia, Fecha_Ultimo_Movto, Id_Articulo, Id_Articulo_Datos, Id_Laboratorio, Id_Linea, 
            Id_Presentacion, IVA, Precio_Venta, Promocionado, Servicio, Ultimo_Precio_Compra, CLAVEPRODSERV, OBJETOIMP) 
            VALUES ({ActualizacionAutomatica}, '{CODIGO_BARRA}', {Costo_Promedio}, '{Des_Abreviado}', {Descontinuado}, '{Descripcion}', 
            {Descuento}, {Exis_Maximo}, {Exis_Minimo}, {Existencia}, '{Fecha}', '{Id_Articulo}', '{Id_Articulo_Datos}', {Id_Laboratorio}, 
            {Id_Linea}, {Id_Presentacion}, {IVA}, {Precio_Venta}, {Promocionado}, {Servicio}, {Ultimo_Precio_Compra},
            '{CLAVEPRODSERV}', {OBJETOIMP})"""
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True

        except Exception as e:
            #posible error
            print('Error: ',e)
            return e
    
    def grabar_datos(self, CONTRAINDICACIONES, DOSIS_ADMINISTRACION, FORMULA, Id_Articulo, INDICACIONES_PROPIEDADES, PRESENTACION):
        try:
            query= f"""INSERT INTO Medicamento_Datos (CONTRAINDICACIONES, DOSIS_ADMINISTRACION, FORMULA, Id_Articulo, INDICACIONES_PROPIEDADES, PRESENTACION)
            VALUES ('{CONTRAINDICACIONES}', '{DOSIS_ADMINISTRACION}', '{FORMULA}', '{Id_Articulo}', '{INDICACIONES_PROPIEDADES}', '{PRESENTACION}')"""
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True

        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def editar(self, ActualizacionAutomatica, CODIGO_BARRA, Costo_Promedio, Des_Abreviado, Descontinuado, Descripcion, Descuento, Exis_Maximo, Exis_Minimo, Existencia, Fecha, Id_Articulo, Id_Articulo_Datos, Id_Laboratorio, Id_Linea, Id_Presentacion, IVA, Precio_Venta, Promocionado, Servicio, Ultimo_Precio_Compra, CLAVEPRODSERV, OBJETOIMP):
        try:
            query= f"""UPDATE Medicamento SET ActualizacionAutomatica = {ActualizacionAutomatica}, 
            CODIGO_BARRA = '{CODIGO_BARRA}', Costo_Promedio = {Costo_Promedio}, Des_Abreviado = '{Des_Abreviado}', 
            Descontinuado = {Descontinuado}, Descripcion = '{Descripcion}', Descuento = {Descuento}, 
            Exis_Maximo = {Exis_Maximo}, Exis_Minimo = {Exis_Minimo}, Existencia = {Existencia}, 
            Fecha_Ultimo_Movto = '{Fecha}', Id_Articulo = '{Id_Articulo}', Id_Articulo_Datos = '{Id_Articulo_Datos}', Id_Laboratorio = {Id_Laboratorio}, 
            Id_Linea = {Id_Linea}, Id_Presentacion = {Id_Presentacion}, IVA = {IVA}, Precio_Venta = {Precio_Venta}, 
            Promocionado = {Promocionado}, Servicio = {Servicio}, Ultimo_Precio_Compra = {Ultimo_Precio_Compra}, 
            CLAVEPRODSERV = '{CLAVEPRODSERV}', OBJETOIMP = '{OBJETOIMP}' WHERE Id_Articulo = '{Id_Articulo}'"""
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e
     
    def editar_datos(self, CONTRAINDICACIONES, DOSIS_ADMINISTRACION, FORMULA, Id_Articulo, INDICACIONES_PROPIEDADES, PRESENTACION):
        try:
            query= f"""UPDATE Medicamento_Datos SET CONTRAINDICACIONES = '{CONTRAINDICACIONES}', DOSIS_ADMINISTRACION = '{DOSIS_ADMINISTRACION}',
            FORMULA = '{FORMULA}', INDICACIONES_PROPIEDADES = '{INDICACIONES_PROPIEDADES}', PRESENTACION = '{PRESENTACION}' WHERE Id_Articulo = '{Id_Articulo}'"""
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True

        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def modifechamedicamento(self, Fecha, Id_Articulo):
        try:
            query= f"UPDATE Medicamento SET Fecha_Ultimo_Movto = '{Fecha}' where Id_Articulo = '{Id_Articulo}'"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True

        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def consulta_mov(self, Id_Articulo):
        try:
            valida1=False
            conn = connect()
            cursor = conn.cursor()
                
            #VALIDA SI HAY MOVIMIENOS DE MEDICAMENTO
            valida2="select Id_Articulo from Movimientos_Medicamento where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True
            
            #MOVIMIENTO NOTAS
            valida2="select Id_Articulo from Movtos_Nota where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True

            #MOVIMIENTO FACURAS
            valida2="select Id_Articulo from Movtos_Factura where Id_Articulo='Movtos_Factura" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True

            #MOVIMIENTO APARTADO
            valida2="select Id_Articulo from Movtos_Apartado where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True
            
            #MOVIMIENTO COMPRAS
            valida2="select Id_Articulo from Movtos_Compras where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True

            #MEDICAMENTO DATOS
            valida2="select Id_Articulo from Medicamento_Datos where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True

            #ENTRADAS
            valida2="select Id_Articulo from Entradas where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True

            #SALIDAS
            valida2="select Id_Articulo from Salidas where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True

            #ACTUALIZACIONES MEDICAMENTOS
            valida2="select Id_Articulo from Actualizaciones_Medicamentos where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True

            #DETALLE NOTA DE CREDITO
            valida2="select Id_Articulo from DETALLE_NOTA_CREDITO Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True

            #MOVIMIENTOS TRASPASOS SALIDA
            valida2="select Id_Articulo from Movtos_Traspaso_Salida where Id_Articulo='" + Id_Articulo +"'"
            cursor.execute(valida2)
            row = cursor.fetchall()
            if row:
                valida1 = True
            
            return valida1
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def elimina(self, Id_Articulo):
        try:
            query = f"DELETE FROM Medicamento WHERE Id_Articulo='{Id_Articulo}'"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True
        except Exception as e:
            print('Error: ',e)
            return e

    def elimina_datosmedi(self, Id_Articulo):
        try:
            query = f"DELETE FROM Medicamento_Datos WHERE Id_Articulo='{Id_Articulo}'"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True
        except Exception as e:
            print('Error: ',e)
            return e
        
    def consulta(self, Id_Articulo, Codigo_Barra, Laboratorio, Descripcion):
        try:
            query = f"select * from Medicamento where Id_Articulo = '{Id_Articulo}' or CODIGO_BARRA = '{Codigo_Barra}' or Descripcion = '{Descripcion}' or Id_Laboratorio = {Laboratorio}"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            return row
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def linea(self):
        try:
            query = "select Descripcion, Id_Laboratorio, Id_Linea from Linea"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            insertObjeo = []
            columnames = [column[0] for column in cursor.description]
            for r in row:
                insertObjeo.append(dict(zip(columnames, r)))
            cursor.close()
            return insertObjeo
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def laboratorio(self):
        try:
            query= "select Id_Laboratorio,Nombre from Laboratorio"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            return row
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e

    def presentacion(self):
        try:
            query= "select Id_Presentacion,Descripcion from Presentacion"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            return row
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e
        
    def claveprodserv(self):
        try:
            query = "select CLAVEPRODSERV, DESCRIPCION from CLAVE_PRODUCTOS_SERVICIOS"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            insertObjeo = []
            columnames = [column[0] for column in cursor.description]
            for r in row:
                insertObjeo.append(dict(zip(columnames, r)))
            cursor.close()
            return insertObjeo
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e
    
    def medicamentosdatos(self):
        try:
            query = "SELECT * From Medicamento_Datos"
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            insertado = []
            columnames = [column[0] for column in cursor.description]
            for r in row:
                insertado.append(dict(zip(columnames, r)))
            cursor.close()
            return insertado
        
        except Exception as e:
            #posible error
            print('Error: ',e)
            return e




        