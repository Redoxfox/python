
from sortedlinkedlist import SortedLinkedList

class DeletableSLL(SortedLinkedList):    
    def delete(self, value):
            prev_node = None
            current_node = self._SortedLinkedList__first
            
            for i in range(self._SortedLinkedList__len):    
                if current_node.value != value:
                    break   
                elif current_node.value == value:
                    if prev_node is None:                   
                        self._SortedLinkedList__first = current_node.next_node
                    elif current_node.next_node is None:    
                        prev_node.next_node = None
                        self.__len -= 1                     
                        break                               
                    else:                                   
                        prev_node.next_node = current_node.next_node
                    self._SortedLinkedList__len -= 1
                else:
                    prev_node = current_node
                current_node = current_node.next_node