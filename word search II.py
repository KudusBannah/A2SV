class TrieNode:
    def __init__(self):
        self.is_complete = False
        self.children = {}
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.is_complete = True
        root.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def backtrack(i, j, curr):
            if curr.is_complete:
                ans.append(curr.word)
                curr.is_complete = False
            if min(i, j) < 0 or i >= len(board) or j  >= len(board[0]):
                return
            if board[i][j] not in curr.children:
                return
            
            temp = board[i][j]
            board[i][j] = "#"

            for move in valid_moves:
                x, y = i + move[0], j + move[1]
                backtrack(x, y, curr.children[temp])

            board[i][j] = temp


        valid_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = []
        for i in range(len(board)):        
            for j in range(len(board[0])):
                backtrack(i, j, trie.root)
        return ans