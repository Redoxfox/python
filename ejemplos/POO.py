"""5.2.1. Elementos y Características de la POO
Los elementos de la POO, pueden entenderse como los materiales que necesitamos
para diseñar y programar un sistema, mientras que las características, podrían
asumirse como las herramientas de las cuáles disponemos para construir el
sistema con esos materiales.Entre los elementos principales de la POO,
podremos encontrar a:
5.2.1.1. Clases
Las clases son los modelos sobre los cuáles se construirán nuestros objetos.
Podemos tomar como ejemplo de clases, el gráfico que hicimos en la página 8 de
este documento.
En Python, una clase se define con la instrucción class seguida de un nombre
genérico para el objeto.
class Objeto:
    pass
class Antena:
    pass
class Pelo:
    pass
class Ojo:
    pass
5.2.1.2. Propiedades
Las propiedades, como hemos visto antes, son las características intrínsecas
del objeto. Éstas, se representan a modo de variables, solo que técnicamente,
pasan a denominarse propiedades:"""


class Antena():
    color = ""
    longitud = ""


class Pelo():
    color = ""
    textura = ""


class Ojo():
    forma = ""
    color = ""
    tamanio = ""


class Objeto():
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()  # propiedad compuesta por el objeto objeto Antena
    ojos = Ojo()       # propiedad compuesta por el objeto objeto Ojo
    pelos = Pelo()     # propiedad compuesta por el objeto objeto Pelo


"""5.2.1.3. Métodos
Los métodos son funciones (como las que vimos en el capítulo anterior), solo
que técnicamente se denominan métodos, y representan acciones propias que puede
realizar el objeto (y no otro):"""


class Objeto1():
    color = "verde"
    tamanio = "grande"
    aspecto = "feo"
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()

    def flotar(self):
        pass


"""Notar que el primer parámetro de un método, siempre debe ser self.
5.2.1.4. Objeto
Las clases por sí mismas, no son más que modelos que nos servirán para crear
objetos en concreto. Podemos decir que una clase, es el razonamiento abstracto
de un objeto, mientras que el objeto, es su materialización. A la acción de
crear objetos, se la denomina instanciar una clase y dicha instancia, consiste
en asignar la clase, como valor a una variable:"""


class Objeto2():
    color = "verde"
    tamanio = "grande"
    aspecto = "feo"
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()


def flotar(self):
        print (12)


et = Objeto2()
print (et.color)
print (et.tamanio)
print (et.aspecto)
et.color = "rosa"
print (et.color)

"""5.2.2. Herencia: característica principal de la POO
Como comentamos en el título anterior, algunos objetos comparten las mismas
propiedades y métodos que otro objeto, y además agregan nuevas propiedades y
métodos. A esto se lo denomina herencia: una clase que hereda de otra.
Vale aclarar, que en Python, cuando una clase no hereda de ninguna otra, debe
hacerse heredar de object, que es la clase principal de Python, que define un
objeto."""


class Antena(object):
    color = ""
    longitud = ""


class Pelo(object):
    color = ""
    textura = ""


class Ojo(object):
    forma = ""
    color = ""
    tamanio = ""


class Objeto3(object):
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()


def flotar2(self):
        pass


class Dedo(object):
    longitud = ""
    forma = ""
    color = ""


class Pie(object):
    forma = "esfera"
    color = "color"
    dedos = Dedo()


def saltar(self):
    pass

# NuevoObjeto sí hereda de otra clase: Objeto


class NuevoObjeto(Objeto):
    pie = Pie()

    def saltar(self):
        pass


"""5.2.3. Accediendo a los métodos y propiedades de un objeto
Una vez creado un objeto, es decir, una vez hecha la instancia de clase, es
posible acceder a su métodos y propiedades. Para ello, Python utiliza una
sintaxis muy simple: el nombre del objeto, seguido de punto y la propiedad o
método al cuál se desea acceder:"""

objeto = Pie()
print (objeto.forma)
objeto.color = "Nuevo valor"
variable = objeto.saltar()
print (variable)

#  print (objeto.otro_metodo())
