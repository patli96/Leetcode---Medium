class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        # create a DP array, indexed 1, with dp[0] = 1 as default
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        dp[1] = 1

        # if the (i-1)-th number is in [1, 9], then dp[i] = dp[i - 1]
        # if the int(s[i-2:i]) is in [10, 26], then dp[i] += dp[i - 2]
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
