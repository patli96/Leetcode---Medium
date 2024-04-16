class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        
        common_letters = set([i for i in text1]).intersection(set([i for i in text2]))
        if not common_letters:
            return 0
        
        text_list_1 = [i for i in text1 if i in common_letters]
        text_list_2 = [i for i in text2 if i in common_letters]
        if text_list_1 == text_list_2:
            return len(text_list_1)

        dp = [[0 for _ in range(len(text_list_2) + 1)] for _ in range(len(text_list_1) + 1)]

        for i in range(1, len(text_list_1) + 1):
            for j in range(1, len(text_list_2) + 1):
                if text_list_1[i - 1] == text_list_2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )
        
        return dp[-1][-1]

