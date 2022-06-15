# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        reverse = None
        # 1. move slow to the middle node
        # 2. reverse left-half list
        while fast and fast.next:
            node = slow
            fast = fast.next.next
            slow = slow.next
            
            node.next = reverse
            reverse = node
        
        if fast:
            slow = slow.next
        
        while slow and slow.val == reverse.val:
            reverse, slow = reverse.next, slow.next
        
        return slow == None