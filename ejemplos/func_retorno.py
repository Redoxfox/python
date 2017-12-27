"""4.2. Llamadas de retorno
En Python, es posible (al igual que en la gran mayoría de los lenguajes de
programación), llamar a una función dentro de otra, de forma fija y de la misma
manera que se la llamaría, desde fuera de dicha función:"""


def mi_funcion():
    return "Hola Mundo"


def saludar(nombre, mensaje='Hola'):
    print (mensaje, nombre)
    print (mi_funcion())


saludar('carlos')

"""Sin embargo, es posible que se desee realizar dicha llamada, de manera
dinámica, es decir, desconociendo el nombre de la función a la que se deseará
llamar. A este tipo de acciones, se las denomina llamadas de retorno.
Para conseguir llamar a una función de manera dinámica, Python dispone de dos
funciones nativas: locals() y globals().Ambas funciones, retornan un
diccionario. En el caso de locals(), éste diccionario se compone -justamente-
de todos los elementos de ámbito local, mientras que el de globals(), retorna
lo propio pero a nivel global."""


def funcion():
    return "Hola Mundo"


def llamada_de_retorno(func=""):
    """Llamada de retorno a nivel global"""
    return globals()[func]()


print (llamada_de_retorno("funcion"))

# Llamada de retorno a nivel local
nombre_de_la_funcion = "funcion"
print (locals()[nombre_de_la_funcion]())

"""Si se tienen que pasar argumentos en una llamada retorno, se lo puede hacer
normalmente:"""


def funcion1(nombre):
    return "Hola " + nombre


def llamada_de_retorno(func=""):
    """Llamada de retorno a nivel global"""
    return globals()[func]("Laura")


print (llamada_de_retorno("funcion1"))

# Llamada de retorno a nivel local
nombre_de_la_funcion = "funcion1"
print (locals()[nombre_de_la_funcion]("Facundo"))

"""4.2.1. Saber si una función existe y puede ser llamada
Durante una llamada de retorno, el nombre de la función, puede no ser el
indicado. Entonces, siempre que se deba realizar una llamada de retorno, es
necesario comprobar que ésta exista y pueda ser llamada."""

if nombre_de_la_funcion in locals():
    if callable(locals()[nombre_de_la_funcion]):
        print (locals()[nombre_de_la_funcion]("Emilse"))

"""El operador in, nos permitirá conocer si un elemento se encuentra dentro de
una colección, mientras que la función callable() nos dejará saber si esa
función puede ser llamada."""


def llamada_de_retorno(func=""):
    if func in globals():
        if callable(globals()[func]):
            return globals()[func]("Laura")
    else:
        return "Función no encontrada"


print (llamada_de_retorno("funcion1"))

nombre_de_la_funcion = "funcion2"

if nombre_de_la_funcion in locals():
    if callable(locals()[nombre_de_la_funcion]):
        print (locals()[nombre_de_la_funcion]("Facundo"))
else:
    print ("Función no encontrada")
