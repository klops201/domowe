from typing import Any
#-------------------------------ZADANIE 2--------------------------------------------

class Stack:

    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)
        return value

    def pop(self):
        return self.elements.pop()

    def print(self):
            for x in self.elements:
                print(x)
            return

    def __len__(self):
        return len(self.elements)


                              ############# TESTY ################
stack = Stack()             #test1

assert len(stack) == 0      #Nowo utworzony stos jest pusty

stack.push(3)
stack.push(10)             # Dodanie kolejno 3 elementów tworzy stos
stack.push(1)
assert len(stack) == 3

top_value = stack.pop()     #Szczytowa wartość na stosie ma wartość 1
assert top_value == 1
assert len(stack) == 2       #Stos po zdjęciu szczytowego elementu ma wartość 2



#-------------------------------ZADANIE 3--------------------------------------------
class Queue:

    def __init__(self):
        self.elements = []

    def __str__(self):
        return ', '.join(self.elements)

    def peek(self):
        print(self.elements[0])

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        first = self.elements[0]
        ile = 0
        for x in self.elements:
            ile += 1
        self.elements.pop(0)
        return first

    def print(self):
            for x in self.elements:
                print(x)
            return

    def __len__(self):
        return len(self.elements)

        ############# TESTY ################
queue = Queue()             #test1

assert len(queue) == 0     #Nowo utworzona kolejka FIFO jest pusta

queue.enqueue('klient1')
queue.enqueue('klient2')     #Dodanie 3 elementów twórzy kolejkę FIFO
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
assert client_first == 'klient1'         #Jako pierwszy zostanie obsłużony klient 1.
assert str(queue) == 'klient2, klient3'  #Po "obsłużeniu" pierwszej osoby w kolejce
assert len(queue) == 2                   #zostaną elementy klient2 i klient3
