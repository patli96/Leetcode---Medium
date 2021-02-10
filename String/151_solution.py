class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split(' ')
        s_list = s_list[::-1]
        return ' '.join([word for word in s_list if word])
