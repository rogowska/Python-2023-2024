# Oliwia Rogowska #
#   Zadanie 11    #
#     Python      #
#   19.12.2023    #
###################

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    def search(self, data):
        pass  # klasy O(n)

    # Zwraca łącze do węzła o podanym kluczu lub None.

    def find_min(self):
        pass  # klasy O(n)

    # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.

    def find_max(self):
        pass  # klasy O(n)

    # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.

    def reverse(self):
        pass  # klasy O(n)
    # Odwracanie kolejności węzłów na liście.
