from typing import Any, List

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        # self.children = list
        self.left = None
        self.right = None

    def printtree(self):
        print(self.value)

    def is_leaf(self):
        if self.right != None:
            return bool(False)
        if self.left != None:
            return bool(False)
        else:
            return bool(True)

    # def add(child):



root = TreeNode('F');
root.left = TreeNode('B');
root.right = TreeNode('G');
root.left.left = TreeNode('A');
root.left.right = TreeNode('D');
root.left.right.left = TreeNode('C');
root.left.right.right = TreeNode('E');
root.right.right = TreeNode('I')
root.right.right.left = TreeNode('H')

print(root.left.left.is_leaf())
print(root.left.left.left)
print(root.left.left.right)
# root.left.right.printtree()






https://www.geeksforgeeks.org/binary-tree-data-structure/
