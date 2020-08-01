'''Programa para calcular valores de funcion f(x) = x²-13x+30  en intervalo [3,10]'''
'''Esta funcion puede ser representada como y = x²-13x+30 '''

#Definicion de variables 
yi = 0 #Resultado de la funcion en cada punto del intervalo (iniciacion a cero) 
xi = 3 #Valor de cada punto del intervalo (iniciacion en 3)

'''Definición de ciclo condicionado (while) para iterar cada punto de la funcion y al mismo
tiempo cumplir con la condicion del intervalo [3,10]'''

while(xi >= 2 and xi <= 10):
    #Implementacion de funcion en lenguaje Python
    yi = xi*xi - 13*xi + 30
    #Impresion de valor de para cada punto del intervalo
    print('El valor de la funcion f(', xi ,') =(', xi,')²','-13(',xi,') + 30=', yi)
    #Aumento de valor de xi en 1 para evaluar el siguiente valor
    xi += 1
    
