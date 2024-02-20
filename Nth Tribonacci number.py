class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def check(n):
            if n in memo: return memo[n]
            if n < 1:
                return 0
            if n < 3:
                return 1
            memo[n] = check(n-1) + check(n-2) + check(n-3)
            return memo[n]
        
        return check(n)