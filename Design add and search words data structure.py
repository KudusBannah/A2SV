class TrieNode:
    def __init__(self):
        self.is_complete = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_complete = True

    def search(self, word: str) -> bool:    
    
        def dfs(curr, i):
            if i >= len(word):
                return curr.is_complete
                
            if word[i] == ".":
                for child in curr.children:
                    if dfs(curr.children[child], i+1):
                        return True
                return False
            
            if word[i] not in curr.children:
                return False
            return dfs(curr.children[word[i]], i+1)

        return dfs(self.root, 0)
            
        