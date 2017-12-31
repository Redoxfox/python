filas = int(input("Escriba el numero de filas de la matrix: "))
columnas = int(input("Escriba el numero de filas de la matrix: "))


class matrix:
        def __init__(self):
            self.datos = []
            self.vector = []
            self.vector = [0]*columnas
            # print(self.vector)

            for i in range(filas):
                self.datos.append([0]*columnas)
                # print(self.datos)



        def CambioPivote (self, filas, columnas, fillpivote, *matrx):
            VectorIntercambio = [ ]
            VectorIntercambio = [0]*columnas
            for i in range(filas):
                NuevoPiv = matrx[i][fillpivote]
                if NuevoPiv != 0:
                    for k in range(columnas):
                        VectorIntercambio[k] = matrx[i][k]
            return  VectorIntercambio            
                        

                   


        def MostrarMatrix(self, filas, columnas):

            for i in range(filas):
                for j in range(columnas):
                    self.datos[i][j] = float(input('Ingrese ('+str(i)+','+str(j)+'):'))
                    a = ""
                    b = columnas-1
                    k = 0
                    piv = 0

            for i in range(filas):
                ValorIndice = self.datos[i][i]
                if ValorIndice == 0 :
                    Cambio=self.CambioPivote(filas, columnas, i, self.datos)
                    print (Cambio) 
                piv = 1/self.datos[i][i]
                for k in range(columnas):
                    self.vector[k] = self.datos[i][k]*piv
                    self.datos[i][k] = self.vector[k]
                    print (str(self.datos[i][k])+ '  ' + str(i)+','+str(k) + 'pivote' + '\n')
                
                for j in range(filas):   
                     aux = self.datos[j][i]
                     if j != i:

                        for l in range(columnas):
                            self.datos[j][l] =-aux*self.vector[l]+self.datos[j][l]
                            print (str(aux)+ '  ' + str(j)+','+str(l) + 'Ceros' + '\n')

            # k += 1

            for k in range(filas):
                for j in range(columnas):
                    a += str(self.datos[k][j]) + " "
                    #  print (j)
                if j == b:
                   # print (a + '\n')
                    print (self.datos)
                a = ""
                   


mimatrix = matrix()
mimatrix.MostrarMatrix(filas, columnas)
