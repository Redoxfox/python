import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic

class Dialogo(QDialog):
      def __init__(self):
        QDialog.__init__(self)
        self.resize(300, 300)
        self.etiqueta = QLabel(self)
        uic.loadUi("matrix22.ui", self)
        self.setWindowTitle("Cuadro de diálogo")
        self.calcular.clicked.connect(self.matrix)

      def matrix(self):
        filas = 2
        columnas = 3
        datos = []
        vector = []
        vector = [0] * columnas
        InicialPivote = [0] * columnas
        VerctorPivote = [0] * columnas

        for i in range(2):
            datos.append([0] * 3)

        datos[0][0] = float(self.I11.text())
        datos[0][1] = float(self.I12.text())
        datos[0][2] = float(self.R1.text())
        datos[1][0] = float(self.I21.text())
        datos[1][1] = float(self.I22.text())
        datos[1][2] = float(self.R2.text())
        print('Your name: ' + self.I11.text())

        a = ""
        b = columnas - 1
        k = 0
        piv = 0
        for i in range(filas):
            ValorIndice = datos[i][i]
            if ValorIndice == 0:
               for s in range(filas):
                   NuevoPiv = datos[s][i]
                   if NuevoPiv != 0 and s > i:
                      Cmbio = s

               for x in range(columnas):
                   InicialPivote[x] = datos[i][x]
                   VerctorPivote[x] = datos[Cmbio][x]
                   datos[Cmbio][x] = InicialPivote[x]
                   datos[i][x] = VerctorPivote[x]

        piv = 1 / datos[i][i]
        for k in range(columnas):
            vector[k] = datos[i][k] * piv
            datos[i][k] = vector[k]

        for j in range(filas):
            aux = datos[j][i]
            if j != i:

                for l in range(columnas):
                    datos[j][l] = -aux * vector[l] + datos[j][l]
                    # print (str(aux)+ '  ' + str(j)+','+str(l) + 'Ceros' + '\n')

        for k in range(filas):
            a = str(datos[k][filas]) + " "
            print('Valor de ' + 'X' + str(k + 1) + ' es = ' + str(a) + '\n')

        self.resultado.setText('X1=' + str(datos[0][filas]))
        self.resultado_2.setText('X2=' + str(datos[1][filas]))
        #  print (j)


class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600, 600)
        self.setWindowTitle("Ventana principal")
        self.boton = QPushButton(self)
        self.boton.setText("Resolver matriz 2X2")
        self.boton.resize(200, 30)
        self.dialogo = Dialogo()
        self.boton.clicked.connect(self.abrirDialogo)

    def abrirDialogo(self):
        self.dialogo.etiqueta.setText(" Por favor ingrese valores matriz")
        self.dialogo.exec_()



app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()