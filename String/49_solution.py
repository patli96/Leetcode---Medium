class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0 or len(strs) == 1:
            return [strs]

        d_dict = collections.defaultdict(list)

        for word in strs:
            d_dict[tuple(sorted(word))].append(word)

        return d_dict.values()