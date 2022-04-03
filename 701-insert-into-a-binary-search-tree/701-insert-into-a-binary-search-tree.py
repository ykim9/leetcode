# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
    
        return root
    
    #iterative
    def insertIntoBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newVal = TreeNode(val)
        if not root:
            return newVal
        cur, next = None, root
        while next:
            if next.val > val:
                cur, next = next, next.left
            else:
                cur, next = next, next.right
                
        if cur.val > val: cur.left = newVal
        else: cur.right = newVal
            
        return root