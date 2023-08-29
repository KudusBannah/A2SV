class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        curr, i = 0, 0
        while i < len(s) and curr < len(t):
            if s[i] == t[curr]:
                curr += 1
            i += 1
        return len(t) - (curr)