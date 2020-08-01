import math
print("ingrese numero a evaluar")
n=int(input())

def esprimo(n):
    parar = False
    primo = False
    divisor = 2 #valor inicial de evaluacion
    modulo = 1
    contador = 2
    factor = []
    while(parar == False):
        modulo = n % contador
       
        #print("Division entre %s, %s",resultado,contador)
        if (modulo == 0 ):
            primo = True
            parar = True
            resultado = n / contador
            print(resultado)
            factor.append(resultado)
            factor.append(contador)
            contador += 1
            

        if (contador <= n and parar != True):
            contador += 1
            #print (contador)
    
        if (contador > n ):
            parar = True
    
    return factor

dividendo=0
factores = []
while (dividendo != 1.0):
    factor = esprimo(n)
    dividendo = factor[0]
    factores.append(factor[1])
    n =  dividendo

print(factores)
