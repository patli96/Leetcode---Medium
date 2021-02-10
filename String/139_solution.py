class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if not s:
            return False

        if len(s) == 1:
            return s in wordDict

        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1

        wordSet = set(wordDict)

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet and dp[i] == 1:
                    # print(f'i = {i}\tj = {j}\ts[i:j] = {s[i:j]}')
                    dp[j] = 1
        print(dp)
        return dp[len(s)]



