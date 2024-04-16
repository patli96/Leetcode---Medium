class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        num_sum_list = [0 for _ in range(max(nums) + 1)]
        for i in nums:
            num_sum_list[i] += i
        dp = [0 for _ in range(len(num_sum_list))]
        dp[1] = num_sum_list[1]
        for i in range(2, len(dp)):
            dp[i] = max(
                dp[i -2] + num_sum_list[i],
                dp[i - 1]
            )
        return dp[-1]

        
