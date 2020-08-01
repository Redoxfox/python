import math
print("ingrese numero a evaluar")
n=int(input())

def esprimo(n):
    parar = False
    primo = False
    divisor = 2 #valor inicial de evaluacion
    modulo = 1
    contador = 2
    
    while(parar == False):
        modulo = n % contador
        resultado = n / contador
        #print("Division entre %s, %s",resultado,contador)
        if (modulo == 0 and contador != n):
            primo = True
            parar = True
            contador += 1
            

        if (contador <= n and parar != True):
            contador += 1
            #print (contador)
    
        if (contador > n ):
            parar = True
    
    return primo

mis_primos = []
for i in range(n+1):
    primo = esprimo(i)
    #print(primo)
    if(primo!=True):
        mis_primos.append(i)
    #else:
    #    print("El numero es primo",i)

print(len(mis_primos))
print(mis_primos)
