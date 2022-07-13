# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path=[], target=targetSum):
            if not node: 
                return None
            
            target -= node.val
            path.append(node.val)
            if not node.left and not node.right:
                if target == 0:
                    result.append(path[:])
            else:
                dfs(node.left, path, target)
                dfs(node.right, path, target)
            path.pop()
        result = []
        dfs(root)
        return result
