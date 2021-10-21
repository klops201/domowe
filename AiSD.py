from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None

    def wypisz(self):
        wartosc1 = self.head
        while wartosc1 is not None:
            print(wartosc1.value)
            wartosc1 = wartosc1.next


    def push(self, value1):
        NewNode = Node(value1)
        NewNode.next = self.head
        self.head = NewNode


    # def append(self):
    #     value: Any
    #     if self.head is None:
    #         self.head = node
    #         return
    #     for thisNode in self:
    #         pass
    #     thisNode.next = node

list1 = LinkedList()
# assert list1.head == None # Nowa lista jest pusta


# list1.head = Node('raz')
# n2 = Node('dwa')
# n3 = Node('trzy')         #przykladowe wartosci
# list1.head.next = n2
# n2.next = n3


list1.push(1)
list1.push(0)
assert str(list1) == '0 -> 1'


# list1.head = Node('raz')
# n2 = Node('dwa')
# n3 = Node('trzy')
#
# list1.head.next = n2
# n2.next = n3





list1.wypisz()

