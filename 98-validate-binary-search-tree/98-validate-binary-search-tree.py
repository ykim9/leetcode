# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
#     def _isValid(self, root, minVal=float('-inf'), maxVal=float('inf')):
#         if not root:
#             return True
#         elif root.val <= minVal or root.val >= maxVal:
#             return False
#         return self._isValid(root.left, minVal, root.val) and self._isValid(root.right, root.val, maxVal)
        
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self._isValid(root)
    
    
    def inorder(self, root, result):
        if not root:
            return
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        self.inorder(root, inorder)
        for i in range(len(inorder) -1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True