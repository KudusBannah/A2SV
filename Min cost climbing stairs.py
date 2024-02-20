class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        cost.append(0)

        def dp(n):
            if n < 2:
                return cost[n]

            if n not in memo:
                memo[n] = min(dp(n-1), dp(n-2)) + cost[n]

            return memo[n]

        return dp(len(cost)-1)