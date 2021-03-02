class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if not nums:
            return False

        nums_sum = sum(nums)

        if nums_sum % 2 != 0:
            return False

        target = int(nums_sum / 2)

        dp = [[False for i in range(target + 1)] for j in range(len(nums))]

        # initialize DP array
        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(len(nums)):
            for j in range(1, target + 1):
                if j < nums[i]:
                    if i > 0:
                        dp[i][j] = dp[i - 1][j] or dp[i][j]
                elif j == nums[i]:
                    dp[i][j] = True
                else:
                    if i > 0:
                        dp[i][j] = dp[i - 1][j - nums[i]] or dp[i - 1][j]

        return dp[-1][-1]