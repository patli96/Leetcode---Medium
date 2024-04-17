class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i: j] == s[i: j][::-1]:
                    counter += 1
        return counter

