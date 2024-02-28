class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.min_word = float("inf")

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        self.min_word = min(self.min_word, len(word))
        
    def longest_common_prefix(self):
        curr, prefix = self.root, ""
        while len(curr.children) == 1 and len(prefix) < self.min_word:
            child = list(curr.children.keys())[0]
            prefix += child
            curr = curr.children[child]
        return prefix
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        my_trie = Trie()

        for word in strs:
            my_trie.insert(word)

        return my_trie.longest_common_prefix()
        

