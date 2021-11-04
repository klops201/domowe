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
        while currNode != None:
            print(currNode.value)
            currNode = currNode.next


    def push(self, value1):
        NewNode = Node(value1)
        NewNode.next = self.head
        self.head = NewNode

    def str(self):
        currNode = self.head
        while currNode != None:
            str(currNode.value)
            currNode = currNode.next    #   ????????????????????????????????????????

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

    def insert(self, value3, after):
        y = int(after)
        NewNode = Node(value3)
        currNode = self.head
        while(currNode.next != y):
            NewNode.next = after.next
            after.next = NewNode

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

    def __str__(self):
        currNode = self.head
        values = []
        print(str(currNode.value), end='')
        currNode = currNode.next
        while currNode != None:
            values.append(str(currNode.value))
            print(' ->', str(currNode.value), end='')
            currNode = currNode.next

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
str(list_)
# assert str(list_) == '0 -> 1'

list_.append(9)                  #Metoda append umieszcza elementy na końcu listy
list_.append(10)
# assert str(list_) == '0 -> 1 -> 9 -> 10'

# middle_node = list_.node(at=1)          #Element o indeksie 2 po wywołaniu metody insert
# list_.insert(5, after=middle_node)    # będzie miał wartość 5
# # assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
#
# first_element = list_.node(at=0)
# returned_first_element = list_.pop()    #Metoda remove_last usuwa i zwraca ostatni element listy
# assert first_element.value == returned_first_element
#
# last_element = list_.node(at=3)         #Metoda remove_last usuwa i zwraca ostatni element listy
# returned_last_element = list_.remove_last()
# print(last_element.value)
# assert last_element.value == returned_last_element
# assert str(list_) == '1 -> 5 -> 9'
















# list_.head = Node('raz')
# n2 = Node('dwa')
# n3 = Node('trzy')         #przykladowe wartosci
# list_.head.next = n2
# n2.next = n3

# list_.head = Node(1)
# n2 = Node(2)
# n3 = Node(3)         #test wartosci 2
# list_.head.next = n2
# n2.next = n3

list_.push(1)
list_.push(0)      #test push
# list_.push(-1)
# list_.append(2)

# middleNode = list_.node(at=1)
# print(middleNode)                 #test insert
# list_.insert(5, n2)

# first_element = list_.node(at=0)
# print(first_element)
# returned_first_element = list_.pop()           #test pop
# print(returned_first_element)
# assert first_element == returned_first_element


# last_element = list_.node(at=2)
# print(last_element)
# returned_last_element = list_.remove_last()   #test remove_last
# print(returned_last_element)
# assert last_element == returned_last_element

# second_node = list_.node(at=1)
# print(second_node)                            #test remove
# list_.remove(n2)

# list_.len()                    #test len
# list_.print()                #test print

# assert str(list_) == '0 -> 1'
