import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

# clase hereda de QMainWindows(Constructor Ventanas)
class Ventana(QMainWindow):
    # Metodo constructor de la clase
      def __init__(self):
          # iniciar el objecto QMainWindows
          QMainWindow.__init__(self)
          # Cargar la configuracion del archivo.ui en el objecto
          uic.loadUi("Micel-Experimental.ui", self)

# instancia para iniciar aplicacion
app=QApplication(sys.argv)
# crea un objeto de la clase
_ventana= Ventana()
# mostrar ventana (Objeto creado)
_ventana.show()
# ejecutar la ventana
app.exec_()
