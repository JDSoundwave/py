# Zadanie nr 1

from typing import Any

#klasa Node będzie reprezentacją węzła

class Node:

    value: Any
    next: 'Node'

    # Inicjalizator

    def __init__(self, wartosc: Any, _next: 'Node'):

        self.value = wartosc
        self.next = _next

# klasa LinkedList będzie reprezentacją listy jednokierunkowej

class LinkedList:

    head = Node
    tail = Node

    # Head, Tail 

    def __init__(self):

        self.head = None
        self.tail = None

    # Metody

    # metoda push(self, value: Any) -> None umieści nowy węzeł na początku listy

    def push(self, wartosc: Any):

        obiekt = Node(wartosc, self.head)
        self.head = obiekt

        if self.tail == None:

            self.tail = self.head

    # metoda pop(self) -> Any usunie pierwszy element z listy i go zwróci

    def pop(self):

        czasowy = self.head
        self.head = self.head.next
        return czasowy.value

    # metoda remove_last(self) -> Any usunie ostatni element z listy i go zwróci

    def remove_last(self):

        if self.len() == 1:

            self.head = None
            self.tail = None

        else:

            dl_list = self.len()
            obecny = self.head
            while dl_list > 2:
                obecny = obecny.next
                dl_list -= 1
            czasowy = obecny.next
            obecny.next = None
            return czasowy.value

    # metoda remove(self, after: Node) -> Any usunie z listy następnik węzła przekazanego w parametrze

    def remove(self, after: Node):

        if self.head:

            czasowy = self.head
            
            while czasowy != after and czasowy.next:
                czasowy = czasowy.next
            if czasowy.next:
                czasowy.next = czasowy.next.next

    # metoda append(self, value: Any) -> None umieści nowy węzeł na końcu listy

    def append(self, wartosc: Any):

        obecny = self.head
        while obecny.next:
            obecny = obecny.next
        obecny.next = Node(wartosc, None)
        self.tail = Node(wartosc, None)

    def node(self, at: int):

        if self.len() > at:
            czasowy = at
            obecny = self.head
            while czasowy > 0:
                obecny = obecny.next
                czasowy = czasowy - 1
            return obecny

    # metoda insert(self, value: Any, after: Node) -> None wstawi nowy węzeł tuż za węzłem wskazanym w parametrze

    def insert(self, value: Any, after: Node):

        if self.len() >= after.value:
            czasowy = self.head
            nowy_node = Node(value, after.next)
            while czasowy != after:
                czasowy = czasowy.next
            czasowy.next = nowy_node
            czasowy = Node(after.value, nowy_node)

    def __repr__(self):

        return self.print()

    # funkcja print wywołana na obiekcie listy zawierającym 2 elementy [0, 1] wyświetli na ekranie "0 -> 1"

    def print(self):

        if self.len():
            obecny_node = self.head
            wyjsciowy_string = ""
            while obecny_node is not None:
                wyjsciowy_string += f"{obecny_node.value}"
                if obecny_node.next is not None:
                    wyjsciowy_string += " -> "
                obecny_node = obecny_node.next
            return wyjsciowy_string

    # funkcja len wywołana na obiekcie listy zwróci jej długość

    def len(self):

        if self.head:
            licznik = 1
            obecny = self.head
            while obecny.next:
                obecny = obecny.next
                licznik += 1
            return licznik
        else:
            return None


# Assert

list_ = LinkedList()

assert list_.head is None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at = 1)
list_.insert(5, after = middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at = 0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at = 3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at = 1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

print(list_)