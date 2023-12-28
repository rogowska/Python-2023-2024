from Node import Node


class RBTree:
    """Klasa reprezentująca drzewo czerwono-czarne."""

    def __init__(self, root_data):
        self.nil = Node(None, None, None, "black")
        self.root = Node(self.nil, self.nil, self.nil, "black", root_data)

    def search(self):
        pass

    def minimum(self):
        pass

    def maximum(self):
        pass

    def successor(self):
        pass

    def predecessor(self):
        pass

    def left_rotate(self, x):
        # inicjacja y jako prawego dziecka x
        y = x.right
        # zamiana lewego poddrzewa y na prawe poddrzewo x
        x.right = y.left
        # jeżeli lewe dziecko y istnieje, jego rodzicem jest x
        if y.left != self.nil:
            y.left.parent = x
        # ustalenie że ojcem y jest teraz ojciec x
        y.parent = x.parent
        # jeżeli x było korzeniem, to teraz korzeniem jest y
        if x.parent == self.nil:
            self.root = y
        # a jeżeli x było lewym dzieckiem swojego rodzica, to teraz tym lewym
        # dzieckiem jest y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        # przyłączanie x jako lewe dziecko y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert_fixup(self, node):
        while node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == "red":
                    node.parent.color = "black"
                    y.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                elif node == node.parent.right:
                    node = node.parent
                    self.left_rotate(node)
                node.parent.color = "black"
                node.parent.parent.color = "red"
                self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == "red":
                    node.parent.color = "black"
                    y.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                elif node == node.parent.left:
                    node = node.parent
                    self.right_rotate(node)
                node.parent.color = "black"
                node.parent.parent.color = "red"
                self.left_rotate(node.parent.parent)

    def insert(self, data_to_insert):
        # inicjalizacja x i rodzica dla tworzonego węzła
        x = self.root
        new_parent = self.nil
        # przechodzenie przez drzewo przez porównywanie wartości węzłów i szukanie rodzica dla tworzonego węzła
        while x != self.nil:
            new_parent = x
            if data_to_insert < x.data:
                x = x.left
            else:
                x = x.right
        if data_to_insert < new_parent.data:
            new_parent.left = Node(new_parent, self.nil, self.nil, "red", data_to_insert)
            self.insert_fixup(new_parent.left)
        else:
            new_parent.right = Node(new_parent, self.nil, self.nil, "red", data_to_insert)
            self.insert_fixup(new_parent.left)

    def transplant(self, node_to_remove, node_to_transplant):
        if node_to_remove.parent == self.nil:
            self.root = node_to_transplant
        elif node_to_remove == node_to_remove.parent.left:
            node_to_remove.parent.left = node_to_transplant
        else:
            node_to_remove.parent.right = node_to_transplant
        node_to_transplant.parent = node_to_remove.parent

    def delete(self):
        pass

    def delete_fixup(self):
        pass
