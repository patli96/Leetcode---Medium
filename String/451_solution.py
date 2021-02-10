class Solution:
    def frequencySort(self, s: str) -> str:

        count_dict = collections.defaultdict(int)

        for letter in set(s):
            count_dict[letter] = s.count(letter)

        ret = ''

        for t in sorted(count_dict.items(), key=lambda item: item[1], reverse=True):
            ret += t[0] * t[1]

        return ret
