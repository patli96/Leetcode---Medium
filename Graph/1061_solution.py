class Solution:

    from collections import defaultdict

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        mapping = defaultdict(lambda: set())

        for i in range(len(s1)):
            mapping[s1[i]].add(s2[i])
            mapping[s2[i]].add(s1[i])
        
        set_list = []
        for key in list(mapping.keys()):
            if key not in mapping.keys():
                continue
            equal_chars = mapping[key]
            traverse_list = list(mapping[key])
            while len(traverse_list) > 0:
                char = traverse_list.pop()
                if char not in mapping:
                    continue
                traverse_list += list(mapping[char])
                equal_chars = equal_chars.union(mapping[char])
                del mapping[char]
            if key in mapping:
                del mapping[key]
            set_list.append(sorted(list(set(equal_chars))))

        ret_str = ""
        for i in baseStr:
            found_flag = False
            for char_set in set_list:
                if i in char_set:
                    ret_str += char_set[0]
                    found_flag = True
                    break
            if found_flag is False:
                ret_str += i
        return ret_str
        
