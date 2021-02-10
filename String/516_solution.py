class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        l = len(s)

        if l == 0 or l == 1:
            return l

        dp = [[0 for i in range(l)] for j in range(l)]

        for i in range(l - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, l):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][l - 1]
