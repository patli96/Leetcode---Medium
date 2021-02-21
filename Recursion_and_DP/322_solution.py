class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        if not coins:
            return -1

        # dp[i] = the minimum number of coins can make up the amount of i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # traverse the dp array, and traverse the coins array on every i
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[-1] == float('inf'):
            return -1

        return dp[-1]
