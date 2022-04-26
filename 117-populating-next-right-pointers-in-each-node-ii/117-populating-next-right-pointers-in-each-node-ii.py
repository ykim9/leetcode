"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        pre = cur = Node(0)
        while node:
            while node:
                cur.next = node.left
                cur = cur.next or cur
                cur.next = node.right
                cur = cur.next or cur
                node = node.next
            node, cur = pre.next, pre
            
        return root
                    
                
            