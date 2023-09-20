class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s) - 1
        def reverse(n):
            if n > (N//2):
                return
            s[n], s[N-n] = s[N-n], s[n]
            reverse(n+1)
        reverse(0)