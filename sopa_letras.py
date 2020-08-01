from random import *

class llenar_palabra:
        
    def letra_aleatorio(self):
        letras = ["A","B","C","D","E","F","G","H","I","J","K","L",
        "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        num_letras = len(letras)-1
        value_letra = randint(0, num_letras)
        letra = letras[value_letra]
        return letra
        #print(num_letras)


    def mapeo_grilla(self, data, palabra, coord_x, coord_y):
        mapeo = llenar_palabra() 
        if coord_x == 0 and coord_y == 0:
           #results = mapeo.mapeo_abj(data, palabra, coord_x, coord_y) 
           #results = mapeo.mapeo_der(data, palabra, coord_x, coord_y) 
           results = mapeo.mapeo_diagonal_der_abj(data, palabra, coord_x, coord_y)
        
        if coord_x == 9 and coord_y == 0:
            #results = mapeo.mapeo_abj(data, palabra, coord_x, coord_y) 
            #results = mapeo.mapeo_der(data, palabra, coord_x, coord_y) 
            results = mapeo.mapeo_diagonal_der_abj(data, palabra, coord_x, coord_y)
            
        print(results)
        
            
            
    
    def llamar_funcion(self, nombres_funcion, data, palabra,coord_x, coord_y):
        seleccionar_funcion = llenar_palabra() 
        if nombres_funcion == "llena_palabra_izq":
            data =  seleccionar_funcion.llena_palabra_izq(data, coord_x, coord_y, palabra)
            return  data
        
        if nombres_funcion == "llena_palabra_der":
            data =  seleccionar_funcion.llena_palabra_der(data, coord_x, coord_y, palabra)
            return  data

        if nombres_funcion == "llena_palabra_arr":
            data =  seleccionar_funcion.llena_palabra_arr(data, coord_x, coord_y, palabra)
            return  data

        if nombres_funcion == "llena_palabra_abj":
            data =  seleccionar_funcion.llena_palabra_abj(data, coord_x, coord_y, palabra)
            return  data

        if nombres_funcion == "llena_palabra_diagonal_izq_abj":
            data =  seleccionar_funcion.llena_palabra_diagonal_izq_abj(data, coord_x, coord_y, palabra)
            return  data

        if nombres_funcion == "llena_palabra_diagonal_izq_arr":
            data =  seleccionar_funcion.llena_palabra_diagonal_izq_arr(data, coord_x, coord_y, palabra)
            return  data

        if nombres_funcion == "llena_palabra_diagonal_der_abj":
            data =  seleccionar_funcion.llena_palabra_diagonal_der_abj(data, coord_x, coord_y, palabra)
            return  data

        if nombres_funcion == "llena_palabra_diagonal_der_arr":
            data =  seleccionar_funcion.llena_palabra_diagonal_der_arr(data, coord_x, coord_y, palabra)
            return  data
        
  

    def llena_palabra_izq(self, sopa_letras, coord_x, coord_y, palabra):
        data = []
        Fill = "completo"
        cont = 0
        for item in palabra:
            coord_y -= 1
            if coord_y >= 0:
                sopa_letras[coord_x][coord_y] = item            
            else:
                Fill = "incompleto"
               
          

        data.append(sopa_letras)
        data.append(Fill)
        
        return data

    def llena_palabra_der(self, sopa_letras, coord_x, coord_y, palabra):
        data = []
        Fill = "completo"
        cont = 0
        for item in palabra:
            coord_y += 1
            if coord_y <= 14:
                sopa_letras[coord_x][coord_y] = item                
            else:
                Fill = "incompleto"
             
        data.append(sopa_letras)
        data.append(Fill)
        
        return data

    def llena_palabra_arr(self, sopa_letras, coord_x, coord_y, palabra):
        data = []
        Fill = "completo"
        cont = 0
        for item in palabra:
            coord_x -= 1
            if coord_x >= 0:
                    sopa_letras[coord_x][coord_y] = item 
            else:
                Fill = "incompleto"
               
        data.append(sopa_letras)
        data.append(Fill)
        
        return data

    def llena_palabra_abj(self, sopa_letras, coord_x, coord_y, palabra):
        data = []
        Fill = "completo"
        cont = 0
        for item in palabra:
            coord_x += 1
            if coord_x <= 14:
                sopa_letras[coord_x][coord_y] = item 
            else:
                Fill = "incompleto"
                
                
        data.append(sopa_letras)
        data.append(Fill)
        
        return data

    def llena_palabra_diagonal_izq_abj(self, sopa_letras, coord_x, coord_y, palabra):
        data = []
        Fill = "completo"
        cont = 0
        for item in palabra:
            coord_x += 1
            coord_y -= 1
            if coord_x <= 14 and coord_y >= 0:
                sopa_letras[coord_x][coord_y] = item 
            else:
                Fill = "incompleto"

        data.append(sopa_letras)
        data.append(Fill)
        
        return data


    def llena_palabra_diagonal_izq_arr(self, sopa_letras, coord_x, coord_y, palabra):
        data = []
        Fill = "completo"
        cont = 0
        for item in palabra:
            coord_x -= 1
            coord_y -= 1
            if coord_x >= 0 and coord_y >= 0:
                sopa_letras[coord_x][coord_y] = item 
            else:
                Fill = "incompleto"
                  
        data.append(sopa_letras)
        data.append(Fill)
        
        return data

    def llena_palabra_diagonal_der_abj(self, sopa_letras, coord_x, coord_y, palabra):
        data = []
        Fill = "completo"
        cont = 0
        for item in palabra:
            coord_x += 1
            coord_y += 1
            if coord_x <= 14 and coord_y <= 14:
                sopa_letras[coord_x][coord_y] = item 
            else:
                Fill = "incompleto"
              
        data.append(sopa_letras)
        data.append(Fill)
        
        return data

    def llena_palabra_diagonal_der_arr(self, sopa_letras, coord_x, coord_y, palabra):
        data = []
        missing_fill = []
        Fill = "completo"
        cont = 0
        for item in palabra:
            coord_x -= 1
            coord_y += 1
            if coord_x >= 0 and coord_y <= 14:
                sopa_letras[coord_x][coord_y] = item 
            else:
                Fill = "incompleto"

        data.append(sopa_letras)
        data.append(Fill)
        
        return data

    def buscar_palabra_izq(self, sopa_letras, palabra):
        value_letra_init = palabra[0]
        coincidencia_exacta = False
        resultado = []
        coordenadas_reales = []
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                parar = False
                considencia =  0
                letter = []
                coordenadas_palabra = []
                if (sopa_letras[coord_refx][coord_refy] == value_letra_init):
                    for item in palabra:
                        if coord_refy >= 0:
                            if sopa_letras[coord_refx][coord_refy] == item:
                                letter.append(item)
                                valor_coordenada = str(coord_refx) + "-" + str(coord_refy)
                                coordenadas_palabra.append(valor_coordenada) 
                                coord_refy -= 1
                                considencia_palabra = "".join(letter) 
                                if considencia_palabra == palabra: 
                                   coordenadas_reales = coordenadas_palabra
                                   coincidencia_exacta = True      
                            else:
                                break
                        else:
                            break 

        resultado.append(coincidencia_exacta)
        resultado.append(coordenadas_reales)       
        return resultado

    def buscar_palabra_der(self, sopa_letras, palabra):
        value_letra_init = palabra[0]
        coincidencia_exacta = False
        resultado = []
        coordenadas_reales = []
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                parar = False
                considencia =  0
                letter = []
                coordenadas_palabra = []
                if (sopa_letras[coord_refx][coord_refy] == value_letra_init):
                    for item in palabra:
                        if coord_refy <= 14:
                            if sopa_letras[coord_refx][coord_refy] == item:
                                letter.append(item) 
                                valor_coordenada = str(coord_refx) + "-" + str(coord_refy)
                                coordenadas_palabra.append(valor_coordenada)   
                                coord_refy += 1
                                considencia_palabra = "".join(letter)   
                                if considencia_palabra == palabra: 
                                   coordenadas_reales = coordenadas_palabra
                                   coincidencia_exacta = True  
                            else:
                                break
                        else:
                            break 
               
        resultado.append(coincidencia_exacta)
        resultado.append(coordenadas_reales)       
        return resultado

    def buscar_palabra_arr(self, sopa_letras, palabra):
        value_letra_init = palabra[0]
        coincidencia_exacta = False
        resultado = []
        coordenadas_reales = []
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                parar = False
                considencia =  0
                letter = []
                coordenadas_palabra = []
                if (sopa_letras[coord_refx][coord_refy] == value_letra_init):
                    for item in palabra:
                        if coord_refy <= 14:
                            if sopa_letras[coord_refx][coord_refy] == item:
                                letter.append(item) 
                                valor_coordenada = str(coord_refx) + "-" + str(coord_refy)
                                coordenadas_palabra.append(valor_coordenada)   
                                coord_refx -= 1
                                considencia_palabra = "".join(letter)   
                                if considencia_palabra == palabra:
                                   coordenadas_reales = coordenadas_palabra 
                                   coincidencia_exacta = True  
                            else:
                                break
                        else:
                            break 
               
        resultado.append(coincidencia_exacta)
        resultado.append(coordenadas_reales)       
        return resultado

    def buscar_palabra_abj(self, sopa_letras, palabra):
        value_letra_init = palabra[0]
        coincidencia_exacta = False
        resultado = []
        coordenadas_reales = []
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                parar = False
                considencia =  0
                letter = []
                coordenadas_palabra = []
                if (sopa_letras[coord_refx][coord_refy] == value_letra_init):
                    for item in palabra:
                        if coord_refx <= 14:
                            if sopa_letras[coord_refx][coord_refy] == item:
                                letter.append(item)
                                valor_coordenada = str(coord_refx) + "-" + str(coord_refy)
                                coordenadas_palabra.append(valor_coordenada)   
                                coord_refx += 1
                                considencia_palabra = "".join(letter)   
                                if considencia_palabra == palabra: 
                                   coordenadas_reales = coordenadas_palabra
                                   coincidencia_exacta = True  
                            else:
                                break
                        else:
                            break 
               
        resultado.append(coincidencia_exacta)
        resultado.append(coordenadas_reales)       
        return resultado

    def buscar_palabra_diagonal_izq_abj(self, sopa_letras, palabra):
        value_letra_init = palabra[0]
        coincidencia_exacta = False
        resultado = []
        coordenadas_reales = []
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                parar = False
                considencia =  0
                letter = []
                coordenadas_palabra = []
                if (sopa_letras[coord_refx][coord_refy] == value_letra_init):
                    for item in palabra:
                        if coord_refx  <= 14 and coord_refy  >= 0:
                            if sopa_letras[coord_refx][coord_refy] == item:
                                letter.append(item)
                                valor_coordenada = str(coord_refx) + "-" + str(coord_refy)
                                coordenadas_palabra.append(valor_coordenada)    
                                coord_refx += 1
                                coord_refy -= 1
                                considencia_palabra = "".join(letter)   
                                if considencia_palabra == palabra: 
                                   coordenadas_reales = coordenadas_palabra
                                   coincidencia_exacta = True  
                            else:
                                break
                        else:
                            break 
               
        resultado.append(coincidencia_exacta)
        resultado.append(coordenadas_reales)       
        return resultado

    def buscar_palabra_diagonal_izq_arr(self, sopa_letras, palabra):
        value_letra_init = palabra[0]
        coincidencia_exacta = False
        resultado = []
        coordenadas_reales = []
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                parar = False
                considencia =  0
                letter = []
                coordenadas_palabra = []
                if (sopa_letras[coord_refx][coord_refy] == value_letra_init):
                    for item in palabra:
                        if coord_refx >= 0 and coord_refy >= 0:
                            if sopa_letras[coord_refx][coord_refy] == item:
                                letter.append(item) 
                                valor_coordenada = str(coord_refx) + "-" + str(coord_refy)
                                coordenadas_palabra.append(valor_coordenada)   
                                coord_refx -= 1
                                coord_refy -= 1
                                considencia_palabra = "".join(letter)   
                                if considencia_palabra == palabra: 
                                   coordenadas_reales = coordenadas_palabra
                                   coincidencia_exacta = True  
                            else:
                                break
                        else:
                            break 
               
        resultado.append(coincidencia_exacta)
        resultado.append(coordenadas_reales)       
        return resultado

    def buscar_palabra_diagonal_der_abj(self, sopa_letras, palabra):
        value_letra_init = palabra[0]
        coincidencia_exacta = False
        resultado = []
        coordenadas_reales = []
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                parar = False
                considencia =  0
                letter = []
                coordenadas_palabra = []
                if (sopa_letras[coord_refx][coord_refy] == value_letra_init):
                    for item in palabra:
                        if coord_refx <= 14 and coord_refy  <= 14:
                            if sopa_letras[coord_refx][coord_refy] == item:
                                letter.append(item) 
                                valor_coordenada = str(coord_refx) + "-" + str(coord_refy)
                                coordenadas_palabra.append(valor_coordenada)   
                                coord_refx += 1
                                coord_refy += 1
                                considencia_palabra = "".join(letter)   
                                if considencia_palabra == palabra:
                                   coordenadas_reales = coordenadas_palabra
                                   coincidencia_exacta = True  
                            else:
                                break
                        else:
                            break 
               
        resultado.append(coincidencia_exacta)
        resultado.append(coordenadas_reales)       
        return resultado

    def buscar_palabra_diagonal_der_arr(self, sopa_letras, palabra):
        value_letra_init = palabra[0]
        coincidencia_exacta = False
        resultado = []
        coordenadas_reales = []
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                parar = False
                considencia =  0
                letter = []
                coordenadas_palabra = []
                if (sopa_letras[coord_refx][coord_refy] == value_letra_init):
                    for item in palabra:
                        if coord_refx >= 0  and coord_refy  <= 14:
                            if sopa_letras[coord_refx][coord_refy] == item:
                                letter.append(item) 
                                valor_coordenada = str(coord_refx) + "-" + str(coord_refy)
                                coordenadas_palabra.append(valor_coordenada)   
                                coord_refx -= 1
                                coord_refy += 1
                                considencia_palabra = "".join(letter)   
                                if considencia_palabra == palabra:
                                   coordenadas_reales = coordenadas_palabra
                                   coincidencia_exacta = True  
                            else:
                                break
                        else:
                            break 
               
        resultado.append(coincidencia_exacta)
        resultado.append(coordenadas_reales)       
        return resultado
                        
    def mapeo_izq(self, data, palabra, coord_x, coord_y):
        letter = []
        opcion = []
        mapeo = True
        valor_metodo = False
        value_letra = palabra[0]
        valor_casilla = data[coord_x][coord_y]
        for item in palabra:
                if value_letra == valor_casilla or valor_casilla == "":
                    letter.append(item)
                    coord_y -= 1
                    if coord_y >= 0:
                        valor_casilla = data[coord_x][coord_y]
                        considencia_palabra = "".join(letter) 
                        if considencia_palabra == palabra: 
                            valor_metodo = True  
                    else:
                        mapeo = False
                else:
                    mapeo = False
                    
        opcion.append(mapeo)   
        opcion.append(valor_metodo)     
              
        return opcion            
    

    def mapeo_der(self, data, palabra, coord_x, coord_y):
        letter = []
        opcion = []
        mapeo = True
        valor_metodo = False
        value_letra = palabra[0]
        valor_casilla = data[coord_x][coord_y]
        for item in palabra:
                if value_letra == valor_casilla or valor_casilla == "":
                    letter.append(item)
                    coord_y += 1
                    if coord_y <= 14:
                        valor_casilla = data[coord_x][coord_y]
                        considencia_palabra = "".join(letter) 
                        if considencia_palabra == palabra: 
                            valor_metodo = True  
                    else:
                        mapeo = False
                else:
                    mapeo = False
                    
        opcion.append(mapeo)   
        opcion.append(valor_metodo)     
              
        return opcion

    def mapeo_abj(self, data, palabra, coord_x, coord_y):
        letter = []
        opcion = []
        mapeo = True
        valor_metodo = False
        value_letra = palabra[0]
        valor_casilla = data[coord_x][coord_y]
        for item in palabra:
                if value_letra == valor_casilla or valor_casilla == "":
                    letter.append(item)
                    coord_x += 1
                    if coord_x <= 14:
                        valor_casilla = data[coord_x][coord_y]
                        considencia_palabra = "".join(letter) 
                        if considencia_palabra == palabra: 
                            valor_metodo = True  
                    else:
                        mapeo = False
                else:
                    mapeo = False
                    
        opcion.append(mapeo)   
        opcion.append(valor_metodo)     
              
        return opcion

    def mapeo_arr(self, data, palabra, coord_x, coord_y):
        letter = []
        opcion = []
        mapeo = True
        valor_metodo = False
        value_letra = palabra[0]
        valor_casilla = data[coord_x][coord_y]
        for item in palabra:
                if value_letra == valor_casilla or valor_casilla == "":
                    letter.append(item)
                    coord_x -= 1
                    if coord_x >= 0:
                        valor_casilla = data[coord_x][coord_y]
                        considencia_palabra = "".join(letter) 
                        if considencia_palabra == palabra: 
                            valor_metodo = True  
                    else:
                        mapeo = False
                else:
                    mapeo = False
                    
        opcion.append(mapeo)   
        opcion.append(valor_metodo)     
              
        return opcion

    def mapeo_diagonal_der_abj(self, data, palabra, coord_x, coord_y):
        letter = []
        opcion = []
        mapeo = True
        valor_metodo = False
        value_letra = palabra[0]
        valor_casilla = data[coord_x][coord_y]
        for item in palabra:
                if value_letra == valor_casilla or valor_casilla == "":
                    letter.append(item)
                    coord_x += 1
                    coord_y += 1
                    if coord_x <=14 and coord_y <=14:
                        valor_casilla = data[coord_x][coord_y]
                        considencia_palabra = "".join(letter) 
                        if considencia_palabra == palabra: 
                            valor_metodo = True  
                    else:
                        mapeo = False
                else:
                    mapeo = False
                    
        opcion.append(mapeo)   
        opcion.append(valor_metodo)     
              
        return opcion

    def mapeo_diagonal_der_arr(self, data, palabra, coord_x, coord_y):
        letter = []
        opcion = []
        mapeo = True
        valor_metodo = False
        value_letra = palabra[0]
        valor_casilla = data[coord_x][coord_y]
        for item in palabra:
                if value_letra == valor_casilla or valor_casilla == "":
                    letter.append(item)
                    coord_x -= 1
                    coord_y += 1
                    if coord_x >= 0 and coord_y <=14:
                        valor_casilla = data[coord_x][coord_y]
                        considencia_palabra = "".join(letter) 
                        if considencia_palabra == palabra: 
                            valor_metodo = True  
                    else:
                        mapeo = False
                else:
                    mapeo = False
                    
        opcion.append(mapeo)   
        opcion.append(valor_metodo)     
              
        return opcion

    def mapeo_diagonal_izq_abj(self, data, palabra, coord_x, coord_y):
        letter = []
        opcion = []
        mapeo = True
        valor_metodo = False
        value_letra = palabra[0]
        valor_casilla = data[coord_x][coord_y]
        for item in palabra:
                if value_letra == valor_casilla or valor_casilla == "":
                    letter.append(item)
                    coord_x += 1
                    coord_y -= 1
                    if coord_x <= 14 and coord_y >= 0:
                        valor_casilla = data[coord_x][coord_y]
                        considencia_palabra = "".join(letter) 
                        if considencia_palabra == palabra: 
                            valor_metodo = True  
                    else:
                        mapeo = False
                else:
                    mapeo = False
                    
        opcion.append(mapeo)   
        opcion.append(valor_metodo)     
              
        return opcion

    def mapeo_diagonal_izq_arr(self, data, palabra, coord_x, coord_y):
        letter = []
        opcion = []
        mapeo = True
        valor_metodo = False
        value_letra = palabra[0]
        valor_casilla = data[coord_x][coord_y]
        for item in palabra:
                if value_letra == valor_casilla or valor_casilla == "":
                    letter.append(item)
                    coord_x -= 1
                    coord_y -= 1
                    if coord_x >= 0 and coord_y >= 0:
                        valor_casilla = data[coord_x][coord_y]
                        considencia_palabra = "".join(letter) 
                        if considencia_palabra == palabra: 
                            valor_metodo = True  
                    else:
                        mapeo = False
                else:
                    mapeo = False
                    
        opcion.append(mapeo)   
        opcion.append(valor_metodo)     
              
        return opcion
         
    def crucigrama(self, palabras):
        data = []

        for i in range(15):
            data.append([])
            for j in range(15):
                data[i].append("")

        nombres_funciones = ["llena_palabra_izq", "llena_palabra_der", "llena_palabra_arr", "llena_palabra_abj",
        "llena_palabra_diagonal_izq_abj", "llena_palabra_diagonal_izq_arr", "llena_palabra_diagonal_der_abj", 
        "llena_palabra_diagonal_der_arr"]
        contador = 0
        index = 0
        numero_palabras = len(palabras)
        lista_palabras_encontradas = []
        while(contador < numero_palabras):
            palabra = palabras[contador]
            parar = False
            iteraciones = 0
            while (parar == False):
                Index_aleatorio = randint(0, 7)
                crucigrama = llenar_palabra()
                if Index_aleatorio == 0:
                    coord_x = randint(0, 14)
                    coord_y = randint(0, 14)
                    mapeo = crucigrama.mapeo_izq(data, palabra, coord_x, coord_y)
                    if mapeo[0] == True and mapeo[1]==True:
                        Nombre_Funcion_Selecionada = nombres_funciones[Index_aleatorio]
                        result_data = crucigrama.llamar_funcion(Nombre_Funcion_Selecionada, data, palabra, coord_x, coord_y)
                        data = result_data[0]
                        fill = result_data[1]
                        if fill == "completo":
                            lista_palabras_encontradas.append(palabra)
                            parar = True
                            contador += 1    
                    else:
                        parar = False
                        fill = "incompleto"
                else:
                    parar = False
                    Index_aleatorio = randint(0, 7) 
            
                if Index_aleatorio == 1:
                    coord_x = randint(0, 14)
                    coord_y = randint(0, 14)
                    mapeo = crucigrama.mapeo_der(data, palabra, coord_x, coord_y)
                    if mapeo[0] == True and mapeo[1]==True:
                        Nombre_Funcion_Selecionada = nombres_funciones[Index_aleatorio]
                        result_data = crucigrama.llamar_funcion(Nombre_Funcion_Selecionada, data, palabra, coord_x, coord_y)
                        data = result_data[0]
                        fill = result_data[1]
                        if fill == "completo":
                            lista_palabras_encontradas.append(palabra)
                            parar = True
                            contador += 1 
                        else:
                            parar = False
                            fill = "incompleto"
                    else:
                        parar = False
                        Index_aleatorio = randint(0, 7) 
            
                if Index_aleatorio == 2:
                    coord_x = randint(0, 14)
                    coord_y = randint(0, 14)
                    mapeo = crucigrama.mapeo_arr(data, palabra, coord_x, coord_y)
                    if mapeo[0] == True and mapeo[1]==True:
                        Nombre_Funcion_Selecionada = nombres_funciones[Index_aleatorio]
                        result_data = crucigrama.llamar_funcion(Nombre_Funcion_Selecionada, data, palabra, coord_x, coord_y)
                        data = result_data[0]
                        fill = result_data[1]
                        if fill == "completo":
                            lista_palabras_encontradas.append(palabra)
                            parar = True
                            contador += 1 
                        else:
                            parar = False
                            fill = "incompleto"
                    else:
                        parar = False
                        Index_aleatorio = randint(0, 7)  
            
                if Index_aleatorio == 3:
                    coord_x = randint(0, 14)
                    coord_y = randint(0, 14)
                    mapeo = crucigrama.mapeo_abj(data, palabra, coord_x, coord_y)
                    if mapeo[0] == True and mapeo[1]==True:
                        Nombre_Funcion_Selecionada = nombres_funciones[Index_aleatorio]
                        result_data = crucigrama.llamar_funcion(Nombre_Funcion_Selecionada, data, palabra, coord_x, coord_y)
                        data = result_data[0]
                        fill = result_data[1]
                        if fill == "completo":
                            lista_palabras_encontradas.append(palabra)
                            parar = True
                            contador += 1 
                        else:
                            parar = False
                            fill = "incompleto"
                    else:
                        parar = False
                        Index_aleatorio = randint(0, 7)  
            
                if Index_aleatorio == 4:
                    coord_x = randint(0, 14)
                    coord_y = randint(0, 14)
                    mapeo = crucigrama.mapeo_diagonal_izq_abj(data, palabra, coord_x, coord_y)
                    if mapeo[0] == True and mapeo[1]==True:
                        Nombre_Funcion_Selecionada = nombres_funciones[Index_aleatorio]
                        result_data = crucigrama.llamar_funcion(Nombre_Funcion_Selecionada, data, palabra, coord_x, coord_y)
                        data = result_data[0]
                        fill = result_data[1]
                        if fill == "completo":
                            lista_palabras_encontradas.append(palabra)
                            parar = True
                            contador += 1 
                        else:
                            parar = False
                            fill = "incompleto"
                    else:
                        parar = False
                        Index_aleatorio = randint(0, 7) 
            
                if Index_aleatorio == 5:
                    coord_x = randint(0, 14)
                    coord_y = randint(0, 14)
                    mapeo = crucigrama.mapeo_diagonal_izq_arr(data, palabra, coord_x, coord_y)
                    if mapeo[0] == True and mapeo[1]==True:
                        Nombre_Funcion_Selecionada = nombres_funciones[Index_aleatorio]
                        result_data = crucigrama.llamar_funcion(Nombre_Funcion_Selecionada, data, palabra, coord_x, coord_y)
                        data = result_data[0]
                        fill = result_data[1]
                        if fill == "completo":
                            lista_palabras_encontradas.append(palabra)
                            parar = True
                            contador += 1 
                        else:
                            parar = False
                            fill = "incompleto"
                    else:
                        parar = False
                        Index_aleatorio = randint(0, 7)  

                if Index_aleatorio == 6:
                    coord_x = randint(0, 14)
                    coord_y = randint(0, 14)
                    mapeo = crucigrama.mapeo_diagonal_der_abj(data, palabra, coord_x, coord_y)
                    if mapeo[0] == True and mapeo[1]==True:
                        Nombre_Funcion_Selecionada = nombres_funciones[Index_aleatorio]
                        result_data = crucigrama.llamar_funcion(Nombre_Funcion_Selecionada, data, palabra, coord_x, coord_y)
                        data = result_data[0]
                        fill = result_data[1]
                        if fill == "completo":
                            lista_palabras_encontradas.append(palabra)
                            parar = True
                            contador += 1 
                        else:
                            parar = False
                            fill = "incompleto"
                    else:
                        parar = False
                        Index_aleatorio = randint(0, 7)  
            
                if Index_aleatorio == 7:
                    coord_x = randint(0, 14)
                    coord_y = randint(0, 14)
                    mapeo = crucigrama.mapeo_diagonal_der_arr(data, palabra, coord_x, coord_y)
                    if mapeo[0] == True and mapeo[1]==True:
                        Nombre_Funcion_Selecionada = nombres_funciones[Index_aleatorio]
                        result_data = crucigrama.llamar_funcion(Nombre_Funcion_Selecionada, data, palabra, coord_x, coord_y)
                        data = result_data[0]
                        fill = result_data[1]
                        if fill == "completo":
                            lista_palabras_encontradas.append(palabra)
                            parar = True
                            contador += 1
                        else:
                            parar = False
                            fill = "incompleto" 
                    else:
                        parar = False
                        Index_aleatorio = randint(0, 7)   

        return data   

    
    def generar_crucigrama(self, list_palabras):         
        numero_palabras = 0
        datos_crucigrama = []
        while numero_palabras < 15:
            numero_palabras_crucigrama = []
            palabras_in_crucigrama = "*"
            for item in list_palabras:
                verificar_palabras = llenar_palabra()
                data = verificar_palabras.crucigrama(list_palabras)
                existe_crucigrama_1 = verificar_palabras.buscar_palabra_izq(data, item)
                existe_crucigrama_2 = verificar_palabras.buscar_palabra_der(data, item)
                existe_crucigrama_3 = verificar_palabras.buscar_palabra_arr(data, item) 
                existe_crucigrama_4 = verificar_palabras.buscar_palabra_abj(data, item)
                existe_crucigrama_5 = verificar_palabras.buscar_palabra_diagonal_izq_abj(data, item)
                existe_crucigrama_6 = verificar_palabras.buscar_palabra_diagonal_izq_arr(data, item)
                existe_crucigrama_7 = verificar_palabras.buscar_palabra_diagonal_der_abj(data, item)
                existe_crucigrama_8 = verificar_palabras.buscar_palabra_diagonal_der_arr(data, item) 

                if (existe_crucigrama_1[0]):
                    print("IZQ",item)
                    #print(existe_crucigrama_1[1])
                    coordenadas = "".join(existe_crucigrama_1[1]) 
                    palabras_in_crucigrama += item + coordenadas + "*"
                    numero_palabras_crucigrama.append(item) 
                
                if (existe_crucigrama_2[0]):
                    print("DER",item)
                    #print(existe_crucigrama_2[1])
                    coordenadas = "".join(existe_crucigrama_2[1]) 
                    palabras_in_crucigrama += item + coordenadas + "*"
                    numero_palabras_crucigrama.append(item)
                
                if (existe_crucigrama_3[0]):
                    print("ARR",item)
                    #print(existe_crucigrama_3[1])
                    coordenadas = "".join(existe_crucigrama_3[1]) 
                    palabras_in_crucigrama += item + coordenadas + "*"
                    numero_palabras_crucigrama.append(item)
                
                if (existe_crucigrama_4[0]):
                    print("ABJ",item)
                    #print(existe_crucigrama_4[1])
                    coordenadas = "".join(existe_crucigrama_4[1]) 
                    palabras_in_crucigrama += item + coordenadas + "*"
                    numero_palabras_crucigrama.append(item)
                
                if (existe_crucigrama_5[0]):
                    print("IZQ-ABJ",item)
                    #print(existe_crucigrama_5[1])
                    coordenadas = "".join(existe_crucigrama_5[1]) 
                    palabras_in_crucigrama += item + coordenadas + "*"
                    numero_palabras_crucigrama.append(item)
                
                if (existe_crucigrama_6[0]):
                    print("IZQ-ARR",item)
                    #print(existe_crucigrama_6[1])
                    coordenadas = "".join(existe_crucigrama_6[1]) 
                    palabras_in_crucigrama += item + coordenadas + "*"
                    numero_palabras_crucigrama.append(item)
                
                if (existe_crucigrama_7[0]):
                    print("DER-ABJ",item)
                    #print(existe_crucigrama_7[1])
                    coordenadas = "".join(existe_crucigrama_7[1]) 
                    palabras_in_crucigrama += item + coordenadas + "*"
                    numero_palabras_crucigrama.append(item)
                
                if (existe_crucigrama_8[0]):
                    print("DER-ARR",item)
                    #print(existe_crucigrama_8[1])
                    coordenadas = "".join(existe_crucigrama_8[1]) 
                    palabras_in_crucigrama += item + coordenadas + "*"
                    numero_palabras_crucigrama.append(item) 
            print(data)   
            numero_palabras = len(numero_palabras_crucigrama)

            
        num_letters = len(palabras_in_crucigrama)-1
        palabras_in_crucigrama = palabras_in_crucigrama[1:num_letters]
        ''' print(palabras_in_crucigrama)
            matrix = []
            matrix = palabras_in_crucigrama.split("*")
            print(matrix)
            numero_palabras = len(numero_palabras_crucigrama) '''
        print(data)
        completar_crucigrama = llenar_palabra()
        for fila in range(15):
            for col in range(15):
                coord_refx = fila
                coord_refy = col
                if (data[coord_refx][coord_refy] == ""):
                    letter = completar_crucigrama.letra_aleatorio()
                    data[coord_refx][coord_refy] = letter  
        
        #print(data)
        datos_crucigrama.append(data) 
        datos_crucigrama.append(palabras_in_crucigrama)  
        #numero_palabras = len(numero_palabras_crucigrama)          
        
        return datos_crucigrama

list_palabras = ["ROPA", "SOAP", "STOP", "START", "NAME", "TABLE","SYSTEM","BABY","HOUSE",
                    "BATHROOM","MOUSE","GARDEN","YARD","COMPUTER","SON"]  
resultados_crucigrama = llenar_palabra()
r = resultados_crucigrama.generar_crucigrama(list_palabras)
print(r)
data = r[0]
    
#Creacion de tabla de vocabulario.
#CREATE TABLE vocabulary (id INT PRIMARY KEY,  english VARCHAR(50) NOT NULL, spanish VARCHAR(50) NOT NULL, grupo INT NOT NULL, ejemplos TEXT);
#Creacion de tabla crucigrama
#CREATE TABLE crucigrama (id INT PRIMARY KEY, grupo INT NOT NULL, palabras TEXT NOT NULL);
""" list_palabras = ["ROPA", "SOAP", "STOP", "START", "NAME", "TABLE","SYSTEM","BABY","HOUSE",
            "BATHROOM","MOUSE","GARDEN","YARD","COMPUTER","SON"]  

numero_palabras_crucigrama = []
for item in list_palabras:
    verificar_palabras = llenar_palabra()
    data = verificar_palabras.crucigrama(list_palabras)
    
    existe_crucigrama_1 = verificar_palabras.buscar_palabra_izq(data, item)
    existe_crucigrama_2 = verificar_palabras.buscar_palabra_der(data, item)
    existe_crucigrama_3 = verificar_palabras.buscar_palabra_arr(data, item) 
    existe_crucigrama_4 = verificar_palabras.buscar_palabra_abj(data, item)
    existe_crucigrama_5 = verificar_palabras.buscar_palabra_diagonal_izq_abj(data, item)
    existe_crucigrama_6 = verificar_palabras.buscar_palabra_diagonal_izq_arr(data, item)
    existe_crucigrama_7 = verificar_palabras.buscar_palabra_diagonal_der_abj(data, item)
    existe_crucigrama_8 = verificar_palabras.buscar_palabra_diagonal_der_arr(data, item)  

    if (existe_crucigrama_1[0]):
        print("IZQ",item)
        print(existe_crucigrama_1[1])
        numero_palabras_crucigrama.append(item) 
    
    if (existe_crucigrama_2[0]):
        print("DER",item)
        print(existe_crucigrama_2[1])
        numero_palabras_crucigrama.append(item)
    
    if (existe_crucigrama_3[0]):
        print("ARR",item)
        print(existe_crucigrama_3[1])
        numero_palabras_crucigrama.append(item)
    
    if (existe_crucigrama_4[0]):
        print("ABJ",item)
        print(existe_crucigrama_4[1])
        numero_palabras_crucigrama.append(item)
    
    if (existe_crucigrama_5[0]):
        print("IZQ-ABJ",item)
        print(existe_crucigrama_5[1])
        numero_palabras_crucigrama.append(item)
    
    if (existe_crucigrama_6[0]):
        print("IZQ-ARR",item)
        print(existe_crucigrama_6[1])
        numero_palabras_crucigrama.append(item)
    
    if (existe_crucigrama_7[0]):
        print("DER-ABJ",item)
        print(existe_crucigrama_7[1])
        numero_palabras_crucigrama.append(item)
    
    if (existe_crucigrama_8[0]):
        print("DER-ARR",item)
        print(existe_crucigrama_8[1])
        numero_palabras_crucigrama.append(item) 
    
    if (existe_crucigrama_1):
            print("IZQ",item)
            numero_palabras_crucigrama.append(item)
        
        if (existe_crucigrama_2):
            print("DER",item)
            numero_palabras_crucigrama.append(item)
        
        if (existe_crucigrama_3):
            print("ARR",item)
            numero_palabras_crucigrama.append(item)
        
        if (existe_crucigrama_4):
            print("ABJ",item)
            numero_palabras_crucigrama.append(item)
        
        if (existe_crucigrama_5):
            print("IZQ-ABJ",item)
            numero_palabras_crucigrama.append(item)
        
        if (existe_crucigrama_6):
            print("IZQ-ARR",item)
            numero_palabras_crucigrama.append(item)
        
        if (existe_crucigrama_7):
            print("DER-ABJ",item)
            numero_palabras_crucigrama.append(item)
        
        if (existe_crucigrama_8):
            print("DER-ARR",item)
            numero_palabras_crucigrama.append(item)


    numero_palabras = len(numero_palabras_crucigrama)

completar_crucigrama = llenar_palabra()
for fila in range(15):
    for col in range(15):
        coord_refx = fila
        coord_refy = col
        if (data[coord_refx][coord_refy] == ""):
            letter = completar_crucigrama.letra_aleatorio()
            data[coord_refx][coord_refy] = letter """
x = ["0","1","2","3","4","5","6","7","8","9","10","1","2","3","4"]
print(x)
print(data[0]) 
print(data[1]) 
print(data[2]) 
print(data[3])
print(data[4]) 
print(data[5]) 
print(data[6]) 
print(data[7]) 
print(data[8]) 
print(data[9])       
print(data[10]) 
print(data[11]) 
print(data[12]) 
print(data[13]) 
print(data[14])    
#print(len(numero_palabras_crucigrama)) 
    


      


    

        
    


            

    