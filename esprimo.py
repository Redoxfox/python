import math
print("ingrese numero a evaluar")
n=int(input())

parar = False
primo = False
divisor = 2 #valor inicial de evaluacion
modulo = 1
contador = 2
while(parar == False):
    modulo = n % contador
    resultado = n / contador
    print("Division entre %s, %s",resultado,contador)
    if (modulo == 0 and contador != n):
       primo = True
       parar = True
       contador += 1

    if (contador <= n and parar != True):
        contador += 1
        print (contador)
    
    if (contador > n ):
        parar = True


if(primo==True):
    print("El numero no es primo es divisible entre %s", contador-1)
else:
    print("El munero es primo")


