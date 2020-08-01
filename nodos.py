""" class Nodo():
    def __init__(self, dato):
       self.dato = dato
       self.siguiente = None

class ListaEnlazadaSimple():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def ListaVacia(self):
        return self.primero == None

    def AgregarUltimo(self, dato):
        if self.ListaVacia():
            self.primero = Nodo(dato)
            self.ultimo = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente =  Nodo(dato)

    def AgregarInicio(self, dato):
        if self.ListaVacia():
            self.primero = Nodo(dato)
            self.ultimo = self.primero
        else:
            aux =  Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
    
    def EliminarInicio(self):
        self.primero = self.primero.siguiente

    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
    
    def EliminarUltimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente

        aux.siguiente = None
        self.ultimo = aux

    def EliminarDato(self, dato):
        if self.ListaVacia():
            return self.primero == None
        else:
            actual = self.primero
            previo = None
            encontrado = False
            numeroNodo = 1
            while encontrado == False:
                if actual.siguiente != None:
                    if actual.dato == dato:
                        if actual == self.primero:
                            self.primero = actual.siguiente
                            encontrado = True
                        else:
                            actual = previo
                            actual = actual.siguiente
                            encontrado = True
                    else:
                        previo = actual
                        actual = actual.siguiente
                
                previo = actual
                #print(previo.dato)
                actual = actual.siguiente
                #print(actual.dato)



    def BuscarDato(self, dato):
        DatoBuscado = self.primero
        encontrado = False

        while DatoBuscado != None and not encontrado:
            if DatoBuscado.dato == dato:
                encontrado = True
            else:
                DatoBuscado = DatoBuscado.siguiente
            
        return encontrado

    
            
#f = Nodo(3)
r = ListaEnlazadaSimple()

r.AgregarUltimo(3)
r.AgregarUltimo(4)
r.AgregarUltimo(3)
r.AgregarUltimo(4)
r.AgregarUltimo(7)
''' print('**lista incial**')
r.recorrido()
r.EliminarUltimo()
print('*****************')
print('**lista sin ultimo elemento**')
r.recorrido()
print('*****************')
r.AgregarInicio(8)
r.AgregarInicio(7)
print('**lista insercion elemento**')
r.recorrido()

r.EliminarInicio()
print('**Eliminar primer elemento**')
r.recorrido()
print(r.BuscarDato(9))

print('*****************') '''
r.AgregarInicio(8)
r.AgregarInicio(7)


print('**Eliminar  elemento**')
r.recorrido()
r.EliminarDato(4)
print('**Eliminar  elemento**')
r.recorrido()
''' print(r.primero)
print(r.ultimo)
print(r.primero.dato)
print(r.ultimo.dato) ''' """

        


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, head):
        self.head = head

    def length(self):
        current = self.head
        if current is not None:
            count = 1

            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0

    def insert(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = linked_list.head
            linked_list.head = new_node
        else:
            current = linked_list.head
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    def delete(self, position):
        if position != 1:
            current = self.head
            k = 1
            while current.next is not None and k < position - 1:
                current = current.next
                k += 1
            if current.next is not None:
                current.next = current.next.next
                return True
            else:
                return False
        else:
            self.head = self.head.next
            return True

#creamos la lista
linked_list = SinglyLinkedList(Node(1))

#rellenamos la lista
for i in range(2,10):
    linked_list.insert(i, i-1)

#insertamos un elemento
linked_list.insert(999,3)

#eliminamos un elemento
linked_list.delete(6)
linked_list.delete(4)

#mostramos la lista
current = linked_list.head
while current is not None:
    print(current.data)
    current = current.next
