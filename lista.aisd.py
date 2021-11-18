from typing import Any

class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def wypisz(self):
        currNode = self.head
        while currNode != None:
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
                # return currNode.value
                return currNode
            licznik += 1
            currNode = currNode.next

        assert(false)
        return 0

    def insert(self, value3, after):
        y = after.value
        NewNode = Node(value3)
        currNode = self.head
        while(currNode.value != y):
            currNode = currNode.next
        NewNode.next = currNode.next
        currNode.next = NewNode

    def pop(self):
        currNode = self.head
        x = currNode.value
        self.head = self.head.next
        currNode.next = self.head
        return x

    def remove_last(self):
        LastNode = self.head
        while(LastNode.next != None):
            LastNode = LastNode.next
        x = LastNode.value

        currNode = self.head
        while(currNode.next.next != None):
            currNode = currNode.next
        LastNode1 = currNode.next
        currNode.next = None
        LastNode1 = None
        return x

    def remove(self, after):

        y = after.value
        currNode = self.head
        while(currNode.value != y):
            currNode = currNode.next
        delNode = currNode.next
        currNode1 = currNode.next.next
        currNode.next = None
        delNode = None

    def __str__(self):
        currNode = self.head
        values = []
        values.append(str(currNode.value))
        while(currNode.next != None):
            currNode = currNode.next
            values.append(str(currNode.value))
        return ' -> '.join(values)

    def __len__(self):
            checkNode = self.head
            licznik = 1
            while(checkNode.next != None):
                checkNode = checkNode.next
                licznik += 1
            print(licznik)

                ############# TESTY ################

list_ = LinkedList()             #test1

assert list_.head == None       # Nowa lista jest pusta

list_.push(1)
list_.push(0)                   #Metoda push umieszcza elementy na początku listy
assert str(list_) == '0 -> 1'

list_.append(9)                  #Metoda append umieszcza elementy na końcu listy
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)    #Element o indeksie 2 po wywołaniu metody insert
list_.insert(5, after=middle_node)    # będzie miał wartość 5
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)       #Metoda pop usuwa i zwraca pierwszy element listy
returned_first_element = list_.pop()
assert first_element.value == returned_first_element

last_element = list_.node(at=3) #Metoda remove_last usuwa i zwraca ostatni element listy
returned_last_element = list_.remove_last()
# list_.wypisz()
assert str(list_) == '1 -> 5 -> 9'


second_node = list_.node(at=1) #Metoda remove przyjmuje węzeł jako argument, a następnie usuwa jego następnik
list_.remove(second_node)
assert str(list_) == '1 -> 5'
