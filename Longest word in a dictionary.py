class TrieNode:
    def __init__(self):
        self.is_complete = False
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.longest_word = ""

    def insert(self, word):
        curr, count = self.root, 0

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            if curr.is_complete: count += 1
        count += 1
        curr.is_complete = True

        if (len(word) == count) and (count > len(self.longest_word)):
            self.longest_word = word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        my_trie = Trie()

        words.sort()
        for word in words:
            my_trie.insert(word)

        return my_trie.longest_word
