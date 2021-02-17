class Solution:
    def numSquares(self, n: int) -> int:

        # find all possible square numbers smaller than the given integer
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        # bottom case
        dp[0] = 0

        # dp
        for i in range(1, n + 1):
            for num in square_nums:
                if i < num:
                    break
                else:
                    dp[i] = min(dp[i - num] + 1, dp[i])

        if dp[-1] == float('inf'):
            return None

        return dp[-1]

