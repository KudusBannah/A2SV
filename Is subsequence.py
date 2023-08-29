class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0
        for letter in s:
            if not letter in t[curr:]:
                return False
            curr += (t[curr:].index(letter) + 1)
        return True