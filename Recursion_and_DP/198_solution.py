class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(len(nums)):
            for j in range(i + 2, len(nums)):
                dp[j] = max(dp[j], nums[j] + dp[i])

        return max(dp)