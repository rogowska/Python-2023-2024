class Node:
    """Klasa reprezentująca węzeł drzewa czerwono-czarnego."""

    def __init__(self, parent, left, right, color, data=None):
        self.data = data
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    # wystarczy porównać wartość danych w węzłach aby stwierdzić ich równość, ponieważ implementacja nie pozwala
    # na duplikaty
    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return not self == other
