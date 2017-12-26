""""Encoding El encoding (o codificación) es otro de los elementos del lenguaje
que no puede omitirse a la hora de hablar de estructuras de control.
Nota El encoding no es más que una directiva que se coloca al inicio de un
archivo Python, a fin de indicar al sistema, la codificación de caracteres
utilizada en el archivo."""
# -*- coding: utf-8 -*-
"""utf-8 podría ser cualquier codificación de caracteres. Si no se indica una
codificación de caracteres, Python podría producir un error si encontrara
caracteres extraños:"""

print ("En el Ñágara encontré un Ñandú")
print ("En el Ñágara encontré un Ñandú")
#  Asignación múltiple
"""Otra de las ventajas que Python nos provee, es la de poder asignar en una
sola instrucción, múltiples variables:"""
a, b, c = 'string', 15, True
"""En una sola instrucción, estamos declarando tres variables: a, b y c y
asignándoles un valor concreto a cada una:"""
print (a)
print (b)
print (c)
"""La asignación múltiple de variables, también puede darse utilizando como
 valores, el contenido de una tupla:"""
mi_tupla = ('hola mundo', 2014)
texto, anio = mi_tupla
print (texto)
print (anio)
mi_lista = ['Argentina', 'Buenos Aires']
pais, provincia = mi_lista
print (pais)
print (provincia)
