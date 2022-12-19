
from conexionBD import *  #Importando conexion BD


#Creando una funcion para obtener la lista de carros.
def listaCarros():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = f"SELECT * FROM carros ORDER BY id DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def updateCarro(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM carros WHERE id = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarCarro(marca='', modelo='', year='', color='', puertas='', favorito=''):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO carros(marca, modelo, year, color, puertas, favorito) VALUES (%s, %s, %s, %s, %s, %s)")
        valores     = (marca, modelo, year, color, puertas, favorito)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        print(cursor.rowcount, "registro Insertado")
        print("1 registro insertado, id", cursor.lastrowid)
        return cursor.rowcount
  

def detallesdelCarro(idCarro):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM carros WHERE id ='%s'" % (idCarro,))
        resultadoQuery = cursor.fetchone()
        
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery
    
    


def  recibeActualizarCarro(marca, modelo, year, color, puertas, favorito, idCarro):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE carros
            SET 
                marca   = %s,
                modelo  = %s,
                year    = %s,
                color   = %s,
                puertas = %s,
                favorito= %s
            WHERE id=%s
            """, (marca,modelo, year, color, puertas, favorito, idCarro ))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        return cur.rowcount
 



def eliminarCarro(idCarro=''):
        
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    cur              = conexion_MySQLdb.cursor(dictionary=True)
    
    cur.execute('DELETE FROM carros WHERE id=%s', (idCarro,))
    conexion_MySQLdb.commit()
    #print(cur.rowcount )
    return cur.rowcount 