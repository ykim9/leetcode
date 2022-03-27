# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = collections.defaultdict(list)
        while head and head.next:
            if head.next in prev[head.val]:
                return True
            else:
                prev[head.val].append(head.next)
            
            head = head.next
        return False