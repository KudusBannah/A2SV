class TrieNode:
    def __init__(self):
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
        
    def is_subsequence(self, word):
        curr = self.root
        for char in word:
            while char not in curr.children:
                children = curr.children.keys()
                if len(children) == 0: return False

                child = list(children)[0]
                curr = curr.children[child]
            curr = curr.children[char]
        return True


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        my_trie = Trie()
        my_trie.insert(s)

        count, word_count = 0, Counter(words)
        for word in word_count:
            ans = int(my_trie.is_subsequence(word)) * word_count[word]
            count += ans

        return count

        