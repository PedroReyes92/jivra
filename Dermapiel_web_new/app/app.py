from flask import Flask, render_template, request, redirect, url_for, session
from flask_paginate import Pagination
from Funciones.login import logeos
from Funciones.usuarios import con_usuarios, farmacias
from Funciones.medicamento import Medicamento
from datetime import datetime


app = Flask(__name__)
app.secret_key = "Jivra.com.mx"

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    data = con_usuarios()
    data2 = farmacias()
    if request.method == 'POST':
        sucursal = request.form['sucursal']
        usuario = request.form['usuario']
        logeo = logeos(usuario, request.form['password'])
        if logeo != None:
            #session.....
            session['usuario'] = usuario
            session['sucursal'] = sucursal
            session['nivel'] = logeo[0][2]
            session['alerta'] = ''
            return redirect(url_for('main'))
        else:
            data3 = "Contraseña Incorrecta."
            return render_template('index.html', data=data, data2=data2, data3=data3)

    else:
        return render_template('index.html', data=data, data2=data2)

@app.route('/main')
def main():
    if 'nivel' in session:
        datos = {'titulo':'Farmacias Dermocutanea'}
        session['alerta'] = ''
        return render_template('main/assets/index.html', datos=datos)
    else:
        return redirect(url_for('login'))

@app.route('/medicamentos', methods=['GET','POST'])
def medicamentos():
    if 'nivel' in session:
        datos ={'titulo':'Medicamentos'}
        if session['alerta'] != '':
            data3 = session['alerta']
            session['alerta'] = ''
            medi = Medicamento()
            linea = medi.linea()
            medicamentosdatos = medi.medicamentosdatos()
            laboratori = medi.laboratorio()
            presentacion = medi.presentacion()
            claveprodserv = medi.claveprodserv()
            total_medi = medi.total()
            total = total_medi[0]
            #pagina actual y reultados por paginas
            page_num = request.args.get('page', 1, type= int)
            per_page = 5
            #calcular indice del primer registro y limiar la consulta a rango de regisros
            start_index= (page_num - 1) * per_page + 1
            start_pagina = start_index - 1
            paginado_medicamentos = medi.todospaginados(per_page,start_pagina)
            #indice del ultimo regisro
            end_index = min(start_index + per_page, total)
            
            if end_index > total:
                end_index = total

            #crear objeto paginable
            paginacion = Pagination(page=page_num, total=total, per_page=per_page, display_msg=f"Medicamentos {start_index} - {end_index} de <strong>({total})</strong>")
            return render_template('main/assets/medicamentos.html', datos=datos, data3=data3, data=paginado_medicamentos, paginacion=paginacion, linea=linea, laboratori=laboratori, presentacion=presentacion, claveprodserv=claveprodserv, datos_medicamentos = medicamentosdatos)
        else:
            medi = Medicamento()
            linea = medi.linea()
            laboratori = medi.laboratorio()
            presentacion = medi.presentacion()
            claveprodserv = medi.claveprodserv()
            medicamentosdatos = medi.medicamentosdatos()
            total_medi = medi.total()
            total = total_medi[0]
            #pagina actual y reultados por paginas
            page_num = request.args.get('page', 1, type= int)
            per_page = 5
            #calcular indice del primer registro y limiar la consulta a rango de regisros
            start_index= (page_num - 1) * per_page + 1
            start_pagina = start_index - 1
            paginado_medicamentos = medi.todospaginados(per_page,start_pagina)
            #indice del ultimo regisro
            end_index = min(start_index + per_page, total)
            
            if end_index > total:
                end_index = total

            #crear objeto paginable
            paginacion = Pagination(page=page_num, total=total, per_page=per_page, display_msg=f"Medicamentos {start_index} - {end_index} de <strong>({total})</strong>")
            return render_template('main/assets/medicamentos.html', datos=datos, data=paginado_medicamentos, paginacion=paginacion, linea=linea, laboratori=laboratori, presentacion=presentacion, claveprodserv=claveprodserv, datos_medicamentos = medicamentosdatos)
    else:
        return redirect(url_for('login'))

@app.route('/grabar_medicamento', methods=['GET', 'POST'])
def grabar_medicamento():
    if request.method == 'POST':
        medi = Medicamento()
        fecha_hora = datetime.now()
        fecha=fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
        id_medi = request.form['Id_medicamento']
        codigo_barra = request.form['Codigo_Barra'] 
        des_abreviada = request.form['Desc_Abreviada']
        descripcion = request.form['Descripcion'] 
        labo = request.form['Laboratorio']
        linea = request.form['Linea']
        presentacion = request.form['Presentacion']
        clave_prod_serv = request.form['Clave_producto_servicios'] 
        maximo = request.form['Maximo'] 
        ult_precio_compra = request.form['Ultimo_Precio_Compra']
        precio_venta = request.form['Precio_Venta'] 
        iva = request.form['Iva'] 
        minimo = request.form['Minimo'] 
        cost_promedio = request.form['Costo_Promedio'] 
        descuento = request.form['Descuento'] 
        existe = medi.existe(id_medi)
        if existe == True:
            session['alerta'] = 'Error: El Id del Articulo ya existe.'
            return redirect(url_for('medicamentos'))
        else:
            grabar_medi = medi.grabar(1, codigo_barra, cost_promedio, des_abreviada, 0, descripcion, descuento, maximo, minimo, 0, fecha, id_medi, id_medi, labo, linea, presentacion, iva, precio_venta, 0, 0, ult_precio_compra, clave_prod_serv, '02')
            if grabar_medi == True:
                session['alerta'] = 'Se ha realizado guardado exitosamente!'
                return redirect(url_for('medicamentos'))
            else:
                session['alerta'] = 'Error: No se han podido realizar los cambios.'
                return redirect(url_for('medicamentos'))
            
@app.route('/editar_medicamento/<string:id_medicamento>', methods=['GET', 'POST'])
def editar_medicamento(id_medicamento):
    if request.method == 'POST':
        medi = Medicamento()
        fecha_hora = datetime.now()
        fecha=fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
        codigo_barra = request.form['Codigo_Barra'] 
        des_abreviada = request.form['Desc_Abreviada']
        descripcion = request.form['Descripcion'] 
        labo = request.form['Laboratorio']
        linea = request.form['Linea']
        presentacion = request.form['Presentacion']
        clave_prod_serv = request.form['Clave_producto_servicios'] 
        maximo = request.form['Maximo'] 
        ult_precio_compra = request.form['Ultimo_Precio_Compra']
        precio_venta = request.form['Precio_Venta'] 
        iva = request.form['Iva'] 
        minimo = request.form['Minimo'] 
        cost_promedio = request.form['Costo_Promedio'] 
        descuento = request.form['Descuento'] 
        editar_medi = medi.editar(1, codigo_barra, cost_promedio, des_abreviada, 0, descripcion, descuento, maximo, minimo, 0, fecha, id_medicamento, id_medicamento, labo, linea, presentacion, iva,precio_venta, 0, 0, ult_precio_compra, clave_prod_serv, '02')
        if editar_medi == True:
            session['alerta'] = 'Se han realizado los cambios exitosamente!'
            return redirect(url_for('medicamentos'))
        else:
            session['alerta'] = 'No se han podido realizar los cambios.'
            return redirect(url_for('medicamentos'))
        
@app.route('/eliminarmedi/<string:id_medicamento>')
def eliminarmedi(id_medicamento):
    medi = Medicamento()
    eliminar = medi.elimina(id_medicamento)
    eliminar_datos = medi.elimina_datosmedi(id_medicamento)

    if eliminar == True and eliminar_datos == True:
        session['alerta'] = 'Se eliminado exitosamente!'
        return redirect(url_for('medicamentos'))
    else:
        session['alerta'] = 'No se han podido realizar los cambios.'
        return redirect(url_for('medicamentos'))          

@app.route('/grabar_datosmedi/<string:id_medicamento>', methods=['GET', 'POST'])
def grabar_datosmedi(id_medicamento):
    if request.method == 'POST':
        medi = Medicamento()
        fecha_hora = datetime.now()
        fecha=fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
        formula = request.form['Formula']
        presentacion = request.form['Presentacion']
        indicacion = request.form['Indicacion']
        contraindicaciones = request.form['Contraindicaciones']
        dosis = request.form['Dosis'] 
        grabar_datosmedicame = medi.grabar_datos(contraindicaciones,dosis,formula,id_medicamento,indicacion,presentacion)
        cambio_fecha = medi.modifechamedicamento(fecha,id_medicamento)
        if grabar_datosmedicame == True and cambio_fecha== True:
            session['alerta'] = 'Se ha realizado guardado exitosamente!'
            return redirect(url_for('medicamentos'))
        else:
            session['alerta'] = 'Error: No se han podido realizar los cambios.'
            return redirect(url_for('medicamentos'))

@app.route('/editar_datosmedi/<string:id_medicamento>', methods=['GET', 'POST'])
def editar_datosmedi(id_medicamento):
    if request.method == 'POST':
        medi = Medicamento()
        fecha_hora = datetime.now()
        fecha=fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
        formula = request.form['Formula']
        presentacion = request.form['Presentacion']
        indicacion = request.form['Indicacion']
        contraindicaciones = request.form['Contraindicaciones']
        dosis = request.form['Dosis']
        editar_datosmedicamentos = medi.editar_datos(contraindicaciones,dosis,formula,id_medicamento,indicacion,presentacion)
        cambio_fecha = medi.modifechamedicamento(fecha,id_medicamento)
        if editar_datosmedicamentos == True and cambio_fecha == True:
            session['alerta'] = 'Se han realizado los cambios exitosamente!'
            return redirect(url_for('medicamentos'))
        else:
            session['alerta'] = 'No se han podido realizar los cambios.'
            return redirect(url_for('medicamentos'))


@app.route('/salir')
def salir():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.127', port=5000)

