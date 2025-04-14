import sys

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

    def inorder(self, node):
        if node != self.NIL:
            # Traverse Left
            self.inorder(node.left)
            # Visit Node
            print(str(node.value) +" , ", end=' ')
            # Traverse Right
            self.inorder(node.right)

    def search_helper(self,node,key):
        if node == self.NIL or key == node.value:
            return node
        if key < node.value:
            return self.search_helper(node.left,key)
        elif key >  node.value:
            return self.search_helper(node.right,key)

    def __print_helper(self, node, indent, last):
        if node != self.NIL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == True else "BLACK"
            print(str(node.value) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def searchTree(self,key):
        return self.search_helper(self.root,key)

    def print_tree(self):
        self.__print_helper(self.root, "", True)

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
        
    def rotate_left(self, x):
        y=x.right
        t2 =y.left

        #Perform Rotation & Update Parents & Their Children
        if t2 != self.NIL:  #if y node has left child
            t2.parent=x
        x.right=t2

        y.left=x
        y.parent=x.parent
        if x.parent is None:  #x is the root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y #Parent of x , its left child is now y node
        else:
            x.parent.right = y #Parent of x , its right child is now y node
        x.parent = y #y is now the parent of x


    def rotate_right(self,x):
        y=x.left
        t2=y.right

        # Perform Rotation & Update Parents & Their Children
        if t2 != self.NIL:
            t2.parent=x
        x.left=t2

        y.parent = x.parent
        if x.parent is None:
            self.root=y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    bst.insert(5)
    bst.insert(9)
    bst.insert(3)
    bst.insert(6)
    bst.insert(7)

    bst.print_tree()