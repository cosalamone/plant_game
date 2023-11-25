import sqlite3

with sqlite3.connect('puntajes.db') as conexion:
    try:
        sentencia = '''create table puntajes
        (
            id integer primary key autoincrement,
            nombre text,
            puntos integer,
            tiempo integer
        )
                '''
        conexion.execute(sentencia)
        print('se creo la tabla puntajes')
    except sqlite3.OperationalError:
        print('La tabla ya existe')

    # INSERT:
    # try: 
    #     conexion.execute('INSERT into puntajes(nombre,puntos,tiempo) values (?,?,?)', ('connie', 1050, 5030))
    #     conexion.execute('INSERT into puntajes(nombre,puntos,tiempo) values (?,?,?)', ('maria', 2050, 5330))
    #     conexion.commit() # Actualiza los datos de la tabla
    # except:
    #     print('Ocurrió un error')

    # SELECT:
    cursor = conexion.execute('SELECT * FROM puntajes')
    for fila in cursor:
        pass
        # print(fila)

    def obtener_top_puntajes():
        cursor = conexion.execute('SELECT * FROM puntajes order by puntos desc LIMIT 5') # obtenidos según puntaje descendente
        puntajes = 'Nombre  -   Puntaje \n'
        for fila in cursor:
            puntajes += f'{fila[1]}  - {fila[2]} \n'
        print(puntajes) 
        return puntajes
    
    def guardar_nuevo_puntaje(nombre,puntos,tiempo):
        try: 
            conexion.execute('INSERT into puntajes(nombre,puntos,tiempo) values (?,?,?)', (nombre, puntos, tiempo))
            conexion.commit() # Actualiza los datos de la tabla
        except:
            print('Ocurrió un error')

# guardar_nuevo_puntaje('pedro',50,1000)
# obtener_puntajes()