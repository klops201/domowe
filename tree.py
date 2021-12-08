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
        self.value = value
        if self.left_child == None:
            self.left_child = BinaryNode(value)

    def add_right_child(self, value):
        self.value = value
        if self.right_child == None:
            self.right_child = BinaryNode(value)

    def traverse_in_order(self, node):
        # self(node)
        if node == None:
            return
        if node.left_child != None:
            self.traverse_in_order(node.left_child)
        x = node.value
        if node.right_child != None:
            self.traverse_in_order(node.right_child)
        return x

    def traverse_post_order(self, node):
        if node == None:
            return
        if node.left_child != None:
            self.traverse_in_order(node.left_child)
        if node.right_child != None:
            self.traverse_in_order(node.right_child)
        x = node.value
        return x

    def traverse_pre_order(self, node):
        if node == None:
            return
        x = node.value
        if node.left_child != None:
            self.traverse_in_order(node.left_child)
        if node.right_child != None:
            self.traverse_in_order(node.right_child)
        return x

    def print(self):
        if self.value == None:
            return
        print(self.left_child.value),print(self.value),print(self.right_child.value)



class BinaryTree:
    def __init__(self):
        self.root = BinaryNode



root = BinaryNode(1)
root.add_left_child(2)
root.add_right_child(3)
root.right_child.add_right_child(7)
root.left_child.add_left_child(4)
root.left_child.add_right_child(5)
root.left_child.left_child.add_left_child(8)
root.left_child.left_child.add_right_child(9)



# root.left_child.left_child = BinaryNode(4)
# root.left_child.right_child = BinaryNode(5)
# root.left_child.left_child.left_child = BinaryNode(8)
# root.left_child.left_child.right_child = BinaryNode(9)
# check = root.left_child.left_child
# print(check.is_leaf())
# root.traverse_post_order(root)
root.print()
