# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        # find the max number and its index
        max_idx = nums.index(max(nums))
        max_val = nums[max_idx]

        # construct the root
        root = TreeNode(val=max_val, left=None, right=None)

        # build children of the root recursively
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])

        return root
