"""Símbolo 	Significado 	Ejemplo 	Resultado
== 	Igual que 	5 == 7 	False
!= 	Distinto que 	rojo != verde 	True
< 	Menor que 	8 < 12 	True
> 	Mayor que 	12 > 7 	True
<= 	Menor o igual que 	12 <= 12 	True
>= 	Mayor o igual que 	4 >= 5 	False
Y para evaluar más de una condición simultáneamente, se utilizan operadores
lógicos:
Operador 	Ejemplo 	Explicación 	Resultado
and 	5 == 7 and 7 < 12 	False and False 	False
and 	9 < 12 and 12 > 7 	True and True 	True
and 	9 < 12 and 12 > 15 	True and False 	False
or 	12 == 12 or 15 < 7 	True or False 	True
or 	7 > 5 or 9 < 12 	True or True 	True
xor 	4 == 4 xor 9 > 3 	True o True 	False
xor 	4 == 4 xor 9 < 3 	True o False 	True

Las estructuras de control de flujo condicionales, se definen mediante el uso
de tres palabras claves reservadas, del lenguaje: if (si), elif (sino, si) y
else (sino).

Veamos algunos ejemplos:

1) Si semáforo esta en verde, cruzar la calle. Sino, esperar."""
semaforo = 'azul'
if semaforo == 'verde':
    print ("Cruzar la calle")
else:
    print ("Esperar")
"""2) Si gasto hasta $100, pago con dinero en efectivo. Si no, si gasto más de
$100 pero menos de $300, pago con tarjeta de débito. Si no, pago con tarjeta
de crédito."""
compra = 200
if compra <= 100:
    print ("Pago en efectivo")
elif compra > 100 and compra < 300:
    print ("Pago con tarjeta de débito")
else:
    print ("Pago con tarjeta de crédito")

"""3) Si la compra es mayor a $100, obtengo un descuento del 10%."""
total_compra = 6
importe_a_pagar = total_compra
if total_compra > 100:
    tasa_descuento = 10
    importe_descuento = total_compra * tasa_descuento / 100
    importe_a_pagar = total_compra - importe_descuento
