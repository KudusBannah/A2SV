class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def canReachTop(curr):
            if curr in memo: return memo[curr]
            
            if curr == 0:
                return 1
            if curr < 0:
                return 0

            memo[curr] = canReachTop(curr-1) + canReachTop(curr-2)
            return memo[curr]
            

        return canReachTop(n)