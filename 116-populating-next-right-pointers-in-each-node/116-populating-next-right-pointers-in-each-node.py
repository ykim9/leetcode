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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root
        
        q = collections.deque([(root.left, root.right)])
        
        while q:
            l, r = q.popleft()
            l.next = r
            if l.left:
                q.append((l.left, l.right))
                q.append((l.right, r.left))
                q.append((r.left, r.right))
                
        return root