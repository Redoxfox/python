
filas = int(input("Escriba el numero de filas de la matrix: "))
columnas = int(input("Escriba el numero de filas de la matrix: "))


class matrix:
        def __init__(self):
            self.datos = []
            self.vector = []
            self.vector = [0]*columnas
            self.InicialPivote = [0]*columnas
            self.VerctorPivote = [0]*columnas

            # print(self.vector)

            for i in range(filas):
                self.datos.append([0]*columnas)
                # print(self.datos)    



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
                    for  s in range(filas):
                         NuevoPiv = self.datos[s][i]
                         if NuevoPiv != 0 and s > i :
                            Cambio=s 

                    for x in range(columnas):
                        self.InicialPivote[x] = self.datos[i][x]
                        self.VerctorPivote[x] = self.datos[Cambio][x]
                        self.datos[Cambio][x] = self.InicialPivote[x]
                        self.datos[i][x] = self.VerctorPivote[x]
                    
                    
                piv = 1/self.datos[i][i]
                for k in range(columnas):
                    self.vector[k] = self.datos[i][k]*piv
                    self.datos[i][k] = self.vector[k]
                    
                
                for j in range(filas):   
                     aux = self.datos[j][i]
                     if j != i:

                        for l in range(columnas):
                            self.datos[j][l] =-aux*self.vector[l]+self.datos[j][l]
                            # print (str(aux)+ '  ' + str(j)+','+str(l) + 'Ceros' + '\n')

            # k += 1

            for k in range(filas):
                a = str(self.datos[k][filas]) + " "
                print ('Valor de ' + 'X' + str(k + 1) + ' es = '+ str(a) + '\n')
                    #  print (j)
   


mimatrix = matrix()
mimatrix.MostrarMatrix(filas, columnas)
