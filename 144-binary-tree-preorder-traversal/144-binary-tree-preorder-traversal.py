# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # root -> left -> right 순 탐색
    # 방법 1: 순환
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node, res):
            if node:
                res.append(node.val)
                preorder(node.left, res)
                preorder(node.right, res)
        result = []
        preorder(root, result)
        return result