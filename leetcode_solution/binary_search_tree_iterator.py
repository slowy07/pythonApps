# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.__stk = []
        self.__traversalLeft(root)
        

    def hasNext(self):
        """
        :rtype: int
        """
        return self.__stk
        
        

    def next(self):
        """
        :rtype: bool
        """
        node = self.__stk.pop()
        self.__traversalLeft(node.right)
        return node.val
    
    def __traversalLeft(self, node):
        while node is not None:
            self.__stk.append(node)
            node = node.left
