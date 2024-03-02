class TrieNode:
    def __init__(self):
        self.is_complete = False
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
        curr.is_complete = True
    
    def find_max_xor(self, word):
        complement = {"0":"1", "1":"0"}

        curr, ans = self.root, ""
        for char in word:
            if complement[char] in curr.children:
                ans += "1"
                curr = curr.children[complement[char]]
            else:
                ans += "0"
                curr = curr.children[char]
        return int(ans, 2)


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        my_trie = Trie()
        max_len = max(nums).bit_length()

        for i in range(len(nums)):
            curr_len = nums[i].bit_length()
            nums[i] = "0" * (max_len-curr_len) + (bin(nums[i])[2:] if nums[i] else "")
            my_trie.insert(nums[i])

        ans = 0
        for num in nums:
            ans = max(ans, my_trie.find_max_xor(num))
        return ans