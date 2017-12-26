"""Mientras que a las listas y tuplas se accede solo y únicamente por un número
de índice, los diccionarios permiten utilizar una clave para declarar y acceder
a un valor:"""
mi_diccionario = {'clave_1': 5, 'clave_2': 6, 'clave_7': 7}
print (mi_diccionario['clave_2'])  # Salida: valor_2
# Un diccionario permite eliminar cualquier entrada:
del(mi_diccionario['clave_7'])
# Al igual que las listas, el diccionario permite modificar los valores
mi_diccionario['clave_1'] = 'Nuevo Valor'
