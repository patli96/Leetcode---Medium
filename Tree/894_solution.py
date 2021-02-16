# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []

            # all trees with left child from FBT(x)
            for x in range(N):
                # all trees with right child from FBT(N - x - 1)
                y = N - 1 - x
                # iterate every one of them and combine them together to form FBT(N)
                # e.g. FBT(5) = FBT(1) + root + FBT(3)
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]
