from __future__ import print_function


class Node:
    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        self.parent = parent

    def getLabel(self):
        return self.label

    def setLabel(self):
        self.label = label
    
     def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        new_node = Node(label, None)