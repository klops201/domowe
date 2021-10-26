from typing import Any

class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:

    def __init__(self):
        self.head = None
        # self.tail = None

    def wypisz(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.value)
            currNode = currNode.next


    def push(self, value1):
        NewNode = Node(value1)
        NewNode.next = self.head
        self.head = NewNode


    def append(self, value2):
        NewNode = Node(value2)

        if self.head == None:
            self.head == NewNode
            return
        LastNode = self.head
        while(LastNode.next):
            LastNode = LastNode.next
        LastNode.next = NewNode

    def node(self, at):
        currNode = self.head
        licznik = 0
        while currNode:
            if(licznik == at):
                return currNode.value
            licznik += 1
            currNode = currNode.next

        assert(false)
        return 0

    def insert(self, value3, afNode):

        NewNode = Node(value3)
        NewNode.next = afNode.next
        afNode.next = NewNode

    def pop(self):
        if (self.head != None):
            currNode = self.head
            return currNode.value
        self.head = self.head.next
        currNode = None

    def remove_last(self):
        LastNode = self.head
        while(LastNode.next != None):
            LastNode = LastNode.next
        return LastNode.value
        LastNode = None

    def remove(self, afNode):
        currNode = self.head
        while (currNode.next != afNode):
            currNode = currNode.next
        afNode.next = None




list1 = LinkedList()        # assert list1.head == None # Nowa lista jest pusta

# list1.head = Node('raz')
# n2 = Node('dwa')
# n3 = Node('trzy')         #przykladowe wartosci
# list1.head.next = n2
# n2.next = n3

list1.head = Node(1)
n2 = Node(2)
n3 = Node(3)         #przykladowe wartosci 2
list1.head.next = n2
n2.next = n3

# list1.push(1)
# list1.push(0)      #sprawdzenie push
# list1.push(-1)
# list1.append(2)

# middleNode = list1.node(at=1)
# print(middleNode)                 #sprawdzenie insert
# list1.insert(5, n2)

# first_element = list1.node(at=0)
# print(first_element)
# returned_first_element = list1.pop()   #sprawdzenie pop
# print(returned_first_element)
# assert first_element == returned_first_element


# last_element = list1.node(at=2)
# print(last_element)
# returned_last_element = list1.remove_last()   #sprawdzenie remove_last
# print(returned_last_element)
# assert last_element == returned_last_element

# second_node = list1.node(at=1)
# print(second_node)                            #sprawdzenie remove
# list1.remove(n2)


list1.wypisz()
