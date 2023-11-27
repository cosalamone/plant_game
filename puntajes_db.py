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

    cursor = conexion.execute('SELECT * FROM puntajes')

    def obtener_top_puntajes():
        cursor = conexion.execute('SELECT * FROM puntajes order by puntos desc LIMIT 5') # obtenidos s/puntaje descendente
        puntos = []
        for fila in cursor:
            puntos.append({'nombre':fila[1], 'puntos': fila[2],'tiempo': fila[3] })
        return puntos
    
    def guardar_nuevo_puntaje(nombre:str,puntos:int,tiempo:int):
        try: 
            conexion.execute('INSERT into puntajes(nombre,puntos,tiempo) values (?,?,?)', (nombre, puntos, tiempo))
            conexion.commit() # Actualiza los datos de la tabla
        except:
            print('Ocurrió un error')
