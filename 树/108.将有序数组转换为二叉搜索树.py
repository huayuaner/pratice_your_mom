# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left= None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 每次取中间值作为节点
        #def dfs(nums):
        if len(nums)<1:
            return None
        mid = len(nums)//2
        val = nums[mid]
        root = TreeNode(val)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
           # return root
        return root