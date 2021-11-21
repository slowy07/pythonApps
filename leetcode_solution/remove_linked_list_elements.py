# Definition for singly-linked list.
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
        
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        dummy.next = head
        prev, curr = dummy, dummy.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        
        return dummy.next
