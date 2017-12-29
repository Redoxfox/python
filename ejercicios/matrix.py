filas = int(input("Escriba el numero de filas de la matrix: "))
columnas = int(input("Escriba el numero de filas de la matrix: "))


class matrix:
        def __init__(self):
            self.datos = []
            for i in range(filas):
                self.datos.append([0]*columnas)
                print(self.datos)

        def MostrarMatrix(self, filas, columnas):

            for i in range(filas):
                for j in range(columnas):
                    self.datos[i][j] = float(input('Ingrese ('+str(i)+','+str(j)+'):'))

                    a = ""
                    b = columnas-1
            for k in range(filas):
                for j in range(columnas):
                    a += str(self.datos[k][j]) + " "
                    #  print (j)
                if j == b:
                    print (a + '\n')
                a = ""
                # print (self.datos)


mimatrix = matrix()
mimatrix.MostrarMatrix(filas, columnas)
