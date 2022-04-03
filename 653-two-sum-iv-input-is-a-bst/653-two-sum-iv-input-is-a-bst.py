# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _find(self, node, nodes, k):
        if not node:
            return False
        
        compliment = k - node.val
        if compliment in nodes:
            return True
        nodes.add(node.val)
        
        return self._find(node.left, nodes, k) or self._find(node.right, nodes, k)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        return self._find(root,set(),k)
        
        