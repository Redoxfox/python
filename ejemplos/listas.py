"""Una lista es similar a una tupla con la diferencia fundamental de que
permite modificar los datos una vez creados:"""
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
"""A las listas se accede igual que a las tuplas, por su número de índice:"""
print (mi_lista[1])   # Salida: 15
print (mi_lista[1:4])  # Devuelve: [15, 2.8, 'otro dato']
print (mi_lista[-2])   # Salida: otro dato
"""Las lista NO son inmutables: permiten modificar los datos una vez
creados:"""
mi_lista[2] = 3.8  # el tercer elemento ahora es 3.8
"""Las listas, a diferencia de las tuplas, permiten agregar nuevos valores:"""
mi_lista.append('Nuevo Dato')
