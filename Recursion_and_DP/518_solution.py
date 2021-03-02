class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        if amount == 0:
            return 1

        if not coins:
            return 0

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        len_coins = len(coins)

        for i in range(len_coins):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[j] += dp[j - coins[i]]

        return dp[-1]