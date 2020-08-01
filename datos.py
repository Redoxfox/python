#Solicitud de ingreso de datos al usuario
print("Por favor ingrese en numero de datos que desea consultar:")
#Leer datos ingresados por el usuario
numeroDatos = int(input())
cont = 1
lista = []
suma = 0
while(cont <= numeroDatos):
    print("Ingrese dato numero",cont)
    x = float(input())
    lista.append(x)
    minimo = min(lista) # Hallar minimo de la forma mas simple con metodos de listas python 
    maximo = max(lista) # Hallar maximo de la forma mas simple con metodos de listas python 
    suma = suma + x
    promedio = suma/numeroDatos
    cont += 1



print("El numero maximo de la lista de numeros es: ",maximo)
print("El numero minimo de la lista de numeros es: ",minimo)
print("La suma de la lista de numeros es: ",suma)
print("El promedio de la lista de numeros es: ",promedio)
    


