from typing import Any, Callable

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return bool(True)
        else:
            return bool(False)

    def add_left_child(self, value):
        if self.left_child == None:
            self.left_child = BinaryNode(value)

    def add_right_child(self, value):
        if self.right_child == None:
            self.right_child = BinaryNode(value)

    def traverse_in_order(self, node):
        if node == None:
            return
        if node.left_child != None:
            self.traverse_in_order(node.left_child)
        print(node.value, end="  ")
        # x = node.value
        if node.right_child != None:
            self.traverse_in_order(node.right_child)
        # return x

    def traverse_post_order(self, node):
        if node == None:
            return
        if node.left_child != None:
            self.traverse_post_order(node.left_child)
        if node.right_child != None:
            self.traverse_post_order(node.right_child)
        print(node.value, end = "  ")
        # x = node.value
        # return x

    def traverse_pre_order(self, node):
        if node == None:
            return
        print(node.value, end = "  ")
        # x = node.value
        if node.left_child != None:
            self.traverse_pre_order(node.left_child)
        if node.right_child != None:
            self.traverse_pre_order(node.right_child)
        # return x

    def print(self):
        if self.value == None:
            return
        # print(self.left_child.value),print(self.value),print(self.right_child.value)
        print(self.value)



class BinaryTree:
    def __init__(self, root):
        self.root = BinaryNode(root)

    def traverse_in_order(self, root):
        if root != None:
            self.root.traverse_in_order(root)

    def traverse_post_order(self, root):
        if root != None:
            self.root.traverse_post_order(root)

    def traverse_pre_order(self, root):
        if root != None:
            self.root.traverse_pre_order(root)

# z = BinaryTree(10)
# assert z.c.value == 10
# z.c.add_right_child(2)
# z.c.add_left_child(9)
# z.c.left_child.add_left_child(1)
# z.c.left_child.add_right_child(3)
# z.c.right_child.add_left_child(4)
# z.c.right_child.add_right_child(6)
# assert z.c.right_child.value == 2
# assert z.c.right_child.is_leaf() is False
# assert z.c.left_child.left_child.value == 1
# assert z.c.left_child.left_child.is_leaf() is True
# c.tra


# print(root.right_child.right_child.is_leaf())
# root.traverse_pre_order(root)

tree = BinaryTree(1)
# root = BinaryNode(1)
tree.root.add_left_child(2)
tree.root.add_right_child(3)
tree.root.right_child.add_right_child(7)
tree.root.left_child.add_left_child(4)
tree.root.left_child.add_right_child(5)
tree.root.left_child.left_child.add_left_child(8)
tree.root.left_child.left_child.add_right_child(9)
# assert tree.root.left_child.left_child.left_child.is_leaf() is True
x = tree.root
print(tree.traverse_in_order(x))
