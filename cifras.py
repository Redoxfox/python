# suma los digitos
def suma(n):
    sumDigit, extNum = 0, 0
    #numEntero = int(input("Ingrese un numero entero: "))
    numEntero = n
    while numEntero != 0:
          extNum = numEntero % 10
          numEntero //= 10
          sumDigit += extNum
    print("El numero aleatorio generado es: {}".format(n))
    print("La suma de los digitos es: {}".format(sumDigit))

#genera los 10 numero aleatorios
import random
for i in range (10):
    numero = random.randint(1,100)
    #Llamado a funcion suma
    suma(numero)
