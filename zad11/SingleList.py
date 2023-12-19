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
        if self.is_empty():
            return None
        else:
            next_node = self.head
            while next_node is not None:
                if next_node.data == data:
                    return next_node
                else:
                    next_node = next_node.next

    def find_min(self):
        if self.is_empty():
            return None
        else:
            min_node = self.head
            next_node = self.head.next
            while next_node is not None:
                if next_node.data < min_node.data:
                    min_node = next_node
                    next_node = next_node.next
            return min_node

    def find_max(self):
        if self.is_empty():
            return None
        else:
            max_node = self.head
            next_node = self.head.next
            while next_node is not None:
                if next_node.data > max_node.data:
                    max_node = next_node
                    next_node = next_node.next
            return max_node

    def reverse(self):
        anode = self.head
        while anode.next is not self.tail:
            temp = anode.next.next
            anode.next.next = anode
            anode = anode.next
            anode.next = temp
        temp = self.head
        self.head = self.tail
        self.tail = temp

