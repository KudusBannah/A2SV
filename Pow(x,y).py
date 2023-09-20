class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def pow(n):
            if n in memo: return memo[n]
            if n == 1: return x
            if n == 0: return 1

            if n % 2 == 0:
                memo[n] = pow(n//2) * pow(n//2)
            else:
                memo[n] = x * pow(n//2) * pow(n//2)
            return memo[n]

        ans = pow(abs(n))
        return 1/ans if n < 0 else ans