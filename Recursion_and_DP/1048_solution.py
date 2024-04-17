class Solution:

     def longestStrChain(self, words: List[str]) -> int:
        max_len_dict = {}
        for word in sorted(words, key=lambda x: len(x)):
            word_max_len = 1
            for i in range(len(word)):
                word_to_check = word[:i] + word[i + 1:]
                if word_to_check in max_len_dict:
                    word_max_len = max(max_len_dict[word_to_check] + 1, word_max_len)
            max_len_dict[word] = word_max_len
        return max(max_len_dict.values())

