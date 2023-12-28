from Node import Node

BLACK = "black"
RED = "red"


class RBTree:
    """Klasa reprezentująca drzewo czerwono-czarne."""

    def __init__(self, root_data):
        self.nil = Node(None, None, None, BLACK)
        self.root = Node(self.nil, self.nil, self.nil, BLACK, root_data)

    def inorder_display(self, root):
        if root:
            self.inorder_display(root.left)
            print(root.data)
            self.inorder_display(root.right)

    def display(self):
        """Funkcja wyświetlająca wartości węzłów w drzewie w kolejności inorder"""
        self.inorder_display(self.root)

    def search(self, data):
        """Funkcja znajdująca węzeł o danej wartości i wracająca ten węzeł jeżeli istnieje, a w przeciwnym
        wypadku nil"""
        current_node = self.root
        node_found = self.nil
        while current_node.data != self.nil or current_node == self.nil:
            if current_node.data == data:
                node_found = current_node
            elif current_node.data < data:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return node_found

    def minimum(self, root=None):
        """Funkcja znajdująca węzeł o najmniejszej wartości dla danego drzewa i zwracająca ten węzeł"""
        if root is None:
            root = self.root
        minimum = root
        while minimum.left != self.nil:
            minimum = minimum.left
        return minimum

    def maximum(self, root=None):
        """Funkcja znajdująca węzeł o największej wartości i zwracająca tą wartość"""
        if root is None:
            root = self.root
        maximum = root
        while maximum.right != self.nil:
            maximum = maximum.right
        return maximum

    def successor(self, node):
        """Funkcja zwracająca następnik węzła pzy przeglądaniu węzła w kolejności inorder"""
        if node.right is not None:
            return self.minimum(node.right)
        parent = node.parent
        while parent is not None:
            if node != parent.right:
                break
            node = parent
            parent = parent.parent
        return parent

    # prawdopodobnie do poprawy
    def predecessor(self, node):
        """Funkcja zwracająca poprzednik węzła pzy przeglądaniu węzła w kolejności inorder"""
        if node.left is not None:
            return self.maximum(node.left)
        parent = node.parent
        while parent is not None:
            if node == parent.right:
                break
            node = parent
            parent = parent.parent
        return parent

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
        while node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                elif node == node.parent.right:
                    node = node.parent
                    self.left_rotate(node)
                node.parent.color = BLACK
                node.parent.parent.color = RED
                self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                elif node == node.parent.left:
                    node = node.parent
                    self.right_rotate(node)
                node.parent.color = BLACK
                node.parent.parent.color = RED
                self.left_rotate(node.parent.parent)

    def insert(self, data_to_insert):
        """Funkcja pozwalająca wstawić węzeł o danej wartości do drzewa"""
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
            new_parent.left = Node(new_parent, self.nil, self.nil, RED, data_to_insert)
            self.insert_fixup(new_parent.left)
        else:
            new_parent.right = Node(new_parent, self.nil, self.nil, RED, data_to_insert)
            self.insert_fixup(new_parent.left)

    def transplant(self, node_to_remove, node_to_transplant):
        if node_to_remove.parent == self.nil:
            self.root = node_to_transplant
        elif node_to_remove == node_to_remove.parent.left:
            node_to_remove.parent.left = node_to_transplant
        else:
            node_to_remove.parent.right = node_to_transplant
        node_to_transplant.parent = node_to_remove.parent

    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                elif w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    self.right_rotate(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = BLACK
                w.right.color = BLACK
                self.right_rotate(x.parent)
                x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.right
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                elif w.left.color == BLACK:
                    w.right.color = BLACK
                    w.color = RED
                    self.left_rotate(w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = BLACK
                w.left.color = BLACK
                self.left_rotate(x.parent)
                x = self.root

    def delete(self, data):
        """Funkcja pozwalająca wstawić węzeł o danej wartości do drzewa"""
        # znalezienie węzła w drzewie o podanej wartości
        y = self.search(data)
        z = y
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self.delete_fixup(x)
