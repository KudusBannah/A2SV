class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1

    def find_word_score(self, word):
        curr, score = self.root, 0
        for char in word:
            curr = curr.children[char]
            score += curr.count
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        my_trie = Trie()
        for word in words:
            my_trie.insert(word)
        
        count = [0] * len(words)
        for i in range(len(words)):
            count[i] = my_trie.find_word_score(words[i])
        return count

        