# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next
            
        tail = head.next if fast else head
        
        is_palindrome = True
        
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            
            tail = tail.next
            
        return is_palindrome
        
