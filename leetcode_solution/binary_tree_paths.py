# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        stk = [(root, str(root.val))]

        while stk:
            curr, path = stk.pop()
            if curr:
                if curr != root:
                    path += "->" + str(curr.val)
                if curr.right:
                    stk.append((curr.right, path))
                if curr.left:
                    stk.append((curr.left, path))
                if not curr.right and not curr.left:
                    res.append(path)

        return res
