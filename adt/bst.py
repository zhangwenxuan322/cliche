# Binary Search Tree

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, i, node):
        if node is None:
            node = Node(i, None, None)
        elif i < node.value:
            node.left = self.insert_node(i, node.left)
        else:
            node.right = self.insert_node(i, node.right)
        return node

    def search_node(self, i, node):
        if node is None:
            return None
        elif i == node.value:
            return node
        elif i < node.value:
            return self.search_node(i, node.left)
        else:
            return self.search_node(i, node.right)

    def bst_insert(self, i):
        self.root = self.insert_node(i, self.root)

    def bst_search(self, i):
        return self.search_node(i, self.root)


bst = BST()
bst.bst_insert(20)
print(bst.root.value)
bst.bst_insert(19)
print(bst.root.left.value)
bst.bst_insert(15)
bst.bst_insert(16)
print(bst.root.left.left.right.value)
print(bst.bst_search(15).value)
