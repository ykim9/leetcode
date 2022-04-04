# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = l = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v = carry
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            
            l.next = ListNode(v%10)
            l = l.next
            carry = v // 10

        return dummy.next
        
            