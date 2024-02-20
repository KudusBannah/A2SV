class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount < 0:
                return float("INF")
            if amount == 0:
                return 0
            
            if amount not in memo:
                min_ = float("INF")
                for coin in coins:
                    min_ = min(min_,  1 + dp(amount-coin))
                memo[amount] = min_
            return memo[amount]

        ans = dp(amount)
        return ans if ans != float("INF") else -1