import csv
import pymysql



resultados = []

Departamentos = ["Amazonas","Antioquia","Arauca","Atlántico","Bolívar","Boyacá","Caldas",
"Caquetá","Casanare","Cauca","Cesar","Chocó","Córdoba","Cundinamarca","Guainía","Guaviare",
"Huila","La Guajira","Magdalena","Meta","Nariño","Norte de Santander","Putumayo","Quindío"
,"Risaralda","San Andrés","Santander","Sucre","Tolima","Valle del Cauca","Vaupés","Vichada"]

def find_word(word, matrix):
    if word in matrix:
        return True
    else:
        return False



#Metodo de conexion a la base de datos############################################ 
def con():
    connection = pymysql.connect(host = "localhost",
                         user="root",
                         password = "Redox2011-*",
                         db = "proyecto",
                         charset = "utf8mb4",
                         cursorclass=pymysql.cursors.DictCursor
                         )
    return connection    


mycon = con()




with open('coordDEP.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    datos = {}
    consulta = []
    cont = 0
    for row in reader:
        id = None
        departamento = row[1]
        latitud = row[2]
        longitud = row[3]
        sql = "INSERT INTO geo_pais (id, departaments, latitud, longitud) VALUES (%s, %s, %s, %s);"
        cursor = mycon.cursor()
        cursor.execute(sql, (id, departamento, latitud, longitud))  
        mycon.commit()  
        print(row[0])
        
    '''datos['departamento'] = row[2]
        datos['latitud'] = row[3]
        datos['longitud'] = row[4]
        datos['id'] = row[0]
        datos['municipio'] = row[1] 
        departameno_in = find_word(datos['departamento'], Departamentos)
        
        if departameno_in:
            cont = cont + 1
            latitud = str(row[3])
            longitud = str(row[4])
            municipio = row[1] 
            indice = Departamentos.index(datos['departamento']) + 1
            departament = str(indice)
            id = str(cont)
        
            consulta.append((id, municipio,  departament, latitud, longitud))
            print(consulta)
            sql = "INSERT INTO `geo_departament` (`id`, `municipio`, `departaments`, `latitud`, `longitud`) VALUES (%s, %s, %s, %s, %s);"
            cursor = mycon.cursor()
            cursor.execute(sql, (id, municipio,  departament, latitud, longitud))  
            mycon.commit()
        else:
            pass
            #print("no existe",  row) 

       
        resultados.append(datos)

    sql = "INSERT INTO geo_departament (id, municipio, departaments, latitud, longitud) VALUES (%s, %s, %s, %s, %s);"
    cursor = mycon.cursor()
    cursor.executemany(sql, consulta)   
    mydb.commit()
    
    print(consulta)  
    sql = "SELECT * from geo_departament"
    cursor = mycon.cursor()
    cursor.execute(sql)
    DatosClient = cursor.fetchall()
    print(DatosClient)   '''      

    


   
    

