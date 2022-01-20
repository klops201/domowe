from enum import Enum
from typing import Optional
from typing import Any
from typing import Dict
from typing import List
from typing import Callable


class Node:
    value: Any
    next: 'Node'

    def __init__(self, v, n):
        self.value = v
        self.next = n

class LinkedList:
    head: Node # początek
    tail: Node # koniec

    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, value: Any) -> None:
        if not self.head:
            self.head = Node(value, None)
            self.tail = self.head
        else:
            e = self.head
            while e:
                if e.next is None:
                    e.next = Node(value, None)
                    e.tail = e.next
                    e = None
                else:
                    e = e.next

    def pop(self) -> Any:
        e = self.head
        self.head = e.next
        return e.value

    def __len__(self):
        e = self.head
        ile = 0
        while e:
            ile = ile + 1
            e = e.next
        return ile

class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self):
        return self._storage.pop()

    def __len__(self):
        return len(self._storage)

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

    def __init__(self, d, i):
        self.data = d
        self.index = i

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight = None):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = dict()

    # dodawanie wierzchołka
    def create_vertex(self, data: Any) -> Vertex:
        i = self.adjacencies.__len__()
        v = Vertex(data, i)
        self.adjacencies[v] = []
        return v

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        if edge == 2:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]):
        odwiedzone = [list(self.adjacencies.keys())[0]]
        kolejka = Queue()
        kolejka.enqueue(list(self.adjacencies.keys())[0])
        while len(kolejka) > 0:
            wierzcholek = kolejka.dequeue()
            visit(wierzcholek)
            for sasiad in self.adjacencies[wierzcholek]:
                if sasiad.destination not in odwiedzone:
                    odwiedzone.append(sasiad.destination)
                    kolejka.enqueue(sasiad.destination)

    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        visit(v)
        visited.append(v)
        for sasiad in self.adjacencies[v]:
            if sasiad.destination not in visited:
                self.dfs(sasiad.destination, visited, visit)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        lista = list(self.adjacencies.keys())[0]
        return self.dfs(lista, [], visit)

    def __str__(self):
        w = ""
        for wierzcholek, sasiady in self.adjacencies.items():
            w += str(wierzcholek.index) + ': ' + wierzcholek.data + '--> ['
            for sasiad in sasiady:
                w = w + str(sasiad.destination.index) + ": " + str(sasiad.destination.data) + ', '
            w += ']\n'
        return w

    def show(self):
        w = ""
        for wierzcholek, sasiady in self.adjacencies.items():
            w += str(wierzcholek.index) + ': ' + wierzcholek.data + '--> ['
            for sasiad in sasiady:
                w = w + str(sasiad.destination.index) + ": " + str(sasiad.destination.data) + ', '
            w += ']\n'
        print(w)

graf = Graph()
VI = graf.create_vertex("VI")
RU = graf.create_vertex("RU")
PA = graf.create_vertex("PA")
CO = graf.create_vertex("CO")
SU = graf.create_vertex("SU")
RA = graf.create_vertex("RA")
CH = graf.create_vertex("CH")
KE = graf.create_vertex("KE")
graf.add_undirected_edge(VI, CH)
graf.add_undirected_edge(VI, RU)
graf.add_undirected_edge(VI, PA)
graf.add_undirected_edge(RU, RA)
graf.add_undirected_edge(RU, SU)
graf.add_undirected_edge(RU, VI)
graf.add_undirected_edge(PA, CO)
graf.add_undirected_edge(PA, KE)
graf.add_undirected_edge(CO, RU)
graf.add_undirected_edge(CO, VI)
graf_2 = Graph()
pies = graf_2.create_vertex("pies")
kot = graf_2.create_vertex("kot")
swinia = graf_2.create_vertex("świnia")
zebra = graf_2.create_vertex("zebra")
graf_2.add_undirected_edge(pies, kot)
graf_2.add_undirected_edge(pies, swinia)
graf_2.add_undirected_edge(kot, zebra)
graf_2.add_undirected_edge(zebra, kot)
graf_3 = Graph()
A = graf_3.create_vertex("A")
B = graf_3.create_vertex("B")
C = graf_3.create_vertex("C")
D = graf_3.create_vertex("D")
E = graf_3.create_vertex("E")
F = graf_3.create_vertex("F")
graf_3.add_undirected_edge(A, B)
graf_3.add_undirected_edge(A, D)
graf_3.add_undirected_edge(A, C)
graf_3.add_undirected_edge(B, A)
graf_3.add_undirected_edge(B, E)
graf_3.add_undirected_edge(B, F)
graf_3.add_undirected_edge(C, A)
graf_3.add_undirected_edge(C, D)
graf_3.add_undirected_edge(E, B)
graf_3.add_undirected_edge(E, F)

def friend_path(g: Graph, f0: Any, f1: Any) -> List[Any]:
    # tworzę pustą kolejke
    kolejka = Queue()
    # dodaje do niej liste z elementem wejściowym f0
    kolejka.enqueue([f0])
    # dopuki kolejka nie będzie pusta
    while kolejka:
        # pobieram i usuwam pierwszy element w kolejce
        sciezka = kolejka.dequeue()
        ostatni_wierzcholek = sciezka[-1]
        # jeżeli ostatni wierzchołek to f1 czyli znaleźliśmy najkrótszą droge
        if ostatni_wierzcholek == f1:
            return sciezka

        # pobieramy wierzchołek na podstawie tekstu
        for k in g.adjacencies.keys():
            if k.data == ostatni_wierzcholek:
                ostatni_wierzcholek = k

        # pętla po sąsiadach wierzchołka
        for sasiad in g.adjacencies[ostatni_wierzcholek]:
            sciezka_2 = list(sciezka)
            sciezka_2.append(sasiad.destination.data)

            # dodajemy do kolejki nową ścieżkę już z dodanym sąsiadem
            kolejka.enqueue(sciezka_2)

def w(v):
    print(v.data)

graf.traverse_depth_first(w)
graf.traverse_breadth_first(w)
graf.show()


print(friend_path(graf, "CH", "VI"))
print(friend_path(graf_2, "pies", "zebra"))
print(friend_path(graf_3, "A", "F"))
