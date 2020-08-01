#importar libreria math para calculos matematicos
import math
#Solicitud de tamaño de n de la matriz 4, 5 etc.. 
columnas = int(input("Ingrese tamaño n de matrix nxn: "))
#Igualar numero de filas con numero de columnas debido a que es una matriz nxn 
filas = columnas

#Creacion de clase matrix para realizar los calculos
class matrix:
        #Metodo constructor de la clase.
        def __init__(self):
            self.datos = []  #Variable de tipo lista para simular matriz vacia
            
            #Ciclo para llenar matriz vacia con zeros
            for i in range(filas):
                self.datos.append([0]*columnas) 

        #Metodo para saber si un numero es primo
        def esprimo(self, n):
            parar = False
            primo = False
            divisor = 2 #valor inicial de evaluacion
            modulo = 1
            contador = 2
    
            while(parar == False):
                modulo = n % contador
                resultado = n / contador
                if (modulo == 0 and contador != n):
                    primo = True
                    parar = True
                    contador += 1
            
                if (contador <= n and parar != True):
                    contador += 1

                if (contador > n ):
                    parar = True
    
            return primo  

        #Metodo para hallar numero de primos de acuerdo al tamaño de la matriz ejm (4x4) tamaño 16    
        def num_primos(self, tam_matrix):
            mis_primos = []
            parar = False
            cont = 0
            while parar != True:
                cont += 1
                primo = matrix.esprimo(self , cont)
                if(primo!=True):
                    mis_primos.append(cont)
                
                if len(mis_primos)==tam_matrix:
                    parar = True
                else:
                    parar = False
            
            return mis_primos

        #Metodo para llenar matriz con numeros primos de acuerdo a tamaño matriz 
        def llenar_matrix(self, columnas):
            filas = columnas 
            tam_matrix = filas * columnas
            primos_in_matrix = matrix.num_primos(self,tam_matrix)
            cont = 0
            for i in range(filas):
                for j in range(columnas):
                    self.datos[i][j] = primos_in_matrix[cont]
                    cont += 1

            print(self.datos)

#Creación de objeto mimatrix de la clase matrix.
mimatrix = matrix()

#Llamada al metodo llenar_matrix de la clase matrix.
mimatrix.llenar_matrix(columnas)
