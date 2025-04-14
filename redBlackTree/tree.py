RED = True
BLACK = False

class RBNode:
    def __init__(self, value, color=RED, left=None, right=None, parent=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def is_red(self):
        return self.color == RED


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(value=None, color=BLACK)
        self.root = self.NIL

    def insert(self, value):
        new_node = RBNode(value=value, left=self.NIL, right=self.NIL, parent=None)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        self.fix_insert(new_node)
    def get_uncle(self, node):
        grandparent = node.parent.parent
        if grandparent is None:
            return None
        if node.parent==grandparent.left:
            return grandparent.right
        else:
            return grandparent.left
        
    def get_uncle(self, node):
        grandparent = node.parent.parent
        if grandparent is None:
            return None
        if node.parent == grandparent.left:
            return grandparent.right
        else:
            return grandparent.left

        
    def fix_insert(self, node):
        if node.parent is None:
            node.color = BLACK
            return

        if node.parent.color == BLACK:
            return

        uncle = self.get_uncle(node)
        parent = node.parent
        grandparent = parent.parent

        if uncle and uncle.color == RED:
            parent.color = BLACK
            uncle.color = BLACK
            grandparent.color = RED
            self.fix_insert(grandparent)
            return

        # Case: Right-Right
        if node == parent.right and parent == grandparent.right:
            self.rotate_left(grandparent)
            parent.color = BLACK
            grandparent.color = RED
            return

        # Case: Left-Left
        if node == parent.left and parent == grandparent.left:
            self.rotate_right(grandparent)
            parent.color = BLACK
            grandparent.color = RED
            return

        # Case: Right-Left
        if node == parent.left and parent == grandparent.right:
            self.rotate_right(parent)
            self.rotate_left(grandparent)
            node.color = BLACK
            grandparent.color = RED
            return

        # Case: Left-Right
        if node == parent.right and parent == grandparent.left:
            self.rotate_left(parent)
            self.rotate_right(grandparent)
            node.color = BLACK
            grandparent.color = RED
            return
        
    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left


