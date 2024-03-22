class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N= len(needle)
        if N > len(haystack): return -1

        sliding_val, needle_val = 0, 0
        for i in range(N):
            sliding_val = (sliding_val + ord(haystack[i]) * (26**(N-1-i))) % (10**9 + 7)
            needle_val = (needle_val + ord(needle[i]) * (26**(N-1-i))) % (10**9 + 7)
        
        if needle_val == sliding_val: return 0
        for l in range(len(haystack)-N):
            r = l + N
            sliding_val = (sliding_val - ord(haystack[l]) * 26**(N-1)) * 26
            sliding_val = (sliding_val + ord(haystack[r])) % (10**9 + 7)

            if sliding_val == needle_val:
                return l + 1
        return -1

        # Rabin Karp Algorithm