# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         def convert(left, right):
#             if left <= right:
#                 mid = (left + right) // 2
#                 node = TreeNode(nums[mid])
#                 node.left = convert(left, mid-1)
#                 node.right = convert(mid+1, right)
#                 return node
#         return convert(0, len(nums) - 1)
    
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node