class TrieNode:
    def __init__(self):
        self.is_complete = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_complete = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - 97
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]

        return curr.is_complete


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            idx = ord(char) - 97
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)