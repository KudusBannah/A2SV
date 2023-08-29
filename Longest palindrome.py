class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_max = 0
        count = 0
        s_count = Counter(s)
        odd = False

        for letter in s_count:
            if s_count[letter] % 2 == 0:
                count += s_count[letter]
            else:
                count += s_count[letter] - 1
                odd = True
        
        return count +1 if odd else count