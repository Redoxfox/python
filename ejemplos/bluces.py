"""2.2.5. Estructuras de control iterativasEste bucle, se encarga de ejecutar
 una misma acción "mientras que" una
determinada condición se cumpla. Ejemplo: Mientras que año sea menor o igual
a 2012, imprimir la frase "Informes del Año año"."""
# -*- coding: utf-8 -*-
anio = 2001
while anio <= 2012:
    print ("Informes del Año", str(anio))
    anio += 1


"""Podrás notar que en cada iteración, incrementamos el valor de la variable
que condiciona el bucle (anio). Si no lo hiciéramos, esta variable siempre
sería igual a 2001 y el bucle se ejecutaría de forma infinita, ya que la
condición (anio <= 2012) siempre se estaría cumpliendo.Pero ¿Qué sucede si el
 valor que condiciona la iteración no es numérico y no puede incrementarse?
 En ese caso, podremos utilizar una estructura de control condicional,
 anidada dentro del bucle, y frenar la ejecución cuando el condicional deje de
 cumplirse, con la palabra clave reservada break:"""

while True:
    nombre = input("Indique su nombre: ")
    if nombre:
        break

"""El bucle anterior, incluye un condicional anidado que verifica si la
variable nombre es verdadera (solo será verdadera si el usuario tipea un
texto en pantalla cuando el nombre le es solicitado). Si es verdadera, el bucle
para (break). Sino, seguirá ejecutándose hasta que el usuario, ingrese un texto
en pantalla.
2.2.5.2. Bucle for
El bucle for, en Python, es aquel que nos permitirá iterar sobre una variable
compleja, del tipo lista o tupla:
1) Por cada nombre en mi_lista, imprimir nombre"""

mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio']
for nombre in mi_lista:
    print (nombre)

#  2) Por cada color en mi_tupla, imprimir color:

mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo')
for color in mi_tupla:
    print (color)

"""En los ejemplos anteriores, nombre y color, son dos variables declaradas en
tiempo de ejecución (es decir, se declaran dinámicamente durante el bucle),
asumiendo como valor, el de cada elemento de la lista (o tupla) en cada
iteración.
Otra forma de iterar con el bucle for, puede emular a while:
3) Por cada año en el rango 2001 a 2013, imprimir la frase "Informes del
Año año":"""

for anio in range(2001, 2013):
    print ("Informes del Año", str(anio))
