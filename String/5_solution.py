class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)

        if str_len == 0:
            return ""

        if str_len == 1:
            return s

        def findPalindrome(i, j, s):
            while i >= 0 and j < str_len and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j]

        max_len = 0
        result = ""
        for i in range(str_len - 1):
            e1 = findPalindrome(i, i, s)
            e2 = findPalindrome(i, i + 1, s)
            if len(e1) > max_len or len(e2) > max_len:
                max_len = max(len(e1), len(e2))
                result = e1 if len(e1) >= len(e2) else e2
        return result