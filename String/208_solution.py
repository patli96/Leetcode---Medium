class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for i in range(len(word)):
            if curr.children[ord(word[i]) - ord('a')] is None:
                curr.children[ord(word[i]) - ord('a')] = TrieNode()
            next_node = curr.children[ord(word[i]) - ord('a')]
            curr = next_node
        curr.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in range(len(word)):
            if curr.children[ord(word[i]) - ord('a')] is None:
                return False
            next_node = curr.children[ord(word[i]) - ord('a')]
            curr = next_node

        if curr.isEnd is True:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for i in range(len(prefix)):
            if curr.children[ord(prefix[i]) - ord('a')] is None:
                return False
            next_node = curr.children[ord(prefix[i]) - ord('a')]
            curr = next_node
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)