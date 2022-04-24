# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self, a, b):
        if a == None or b == None:
            return a == b
        return a.val == b. val and self.isEqual(a.left, b.left) and self.isEqual(a.right, b.right)
    
    def dfs(self, a, b):
        if not a:
            return False
        
        if a.val == b.val and self.isEqual(a, b):
            return True
        
        return self.dfs(a.left, b) or self.dfs(a.right, b)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)