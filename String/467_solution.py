class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:

        if not p:
            return 0

        prepend = ' '
        p = prepend + p

        substr_len_map = defaultdict(int)

        l = 1

        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i - 1]) == 1 or (p[i - 1] == 'z' and p[i] == 'a'):
                l += 1
            else:
                l = 1
            substr_len_map[p[i]] = max(l, substr_len_map[p[i]])

        return sum(substr_len_map.values())