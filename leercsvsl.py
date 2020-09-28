import os

#lista con los nombres de cada archivo en mi caso dos archivos con
#coordenadas geograficas
#Nota: Debes colocar las ubicaciones de los archivos en caso los tengas
#      en directorio distinto donde vas a correr el algoritmo
#      yo no las coloque porque estoy en el mismo directorio.
num_files= ["coordDEP1.csv","coordDEP2.csv"]
#Abrir archivo donde se va a guardar el consolidado 
consolidado = open("consolidado.csv", 'w+')
#Agregar cabecera que segun el enunciado debe ser igual en todos los archivos
consolidado.write("num,depar,altitud,long")



#Cliclo for para ir recorriendo contenido de cada archivo y no abrirlos en simultaneo
for file in num_files:
    #Salto de linea
    
    consolidado.write("\n")
    name_file = file
    #contador para saber que linea se esta leyendo
    cont = 0
    #Abrir archivo segun el for que va ir abriendo cada archivo de la lista segun su nombre
    with open(name_file, 'r') as f:
        #Ciclo para leer cada linea del archivo abierto actualmente
        for linea in f:
            #si contador es 0 entonces no se tiene en copia esto es para eliminar el encabezado de 
            # cada archivo
            if cont > 0:
                #Se escribe linea actual en archivo consolidado # primera linea
                consolidado.write(linea)

            #Aumentar contador de linea    
            cont += 1    
    #Cierre de archivo actual de la lista de archivos para liberar buffer
    # y poder abrir el siguiente archivo   
    f.close()  

#Cierre de archivo consolidado para liberar buffer.
consolidado.close()  
    