class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @cache
        def dp(bought, i):
            if i >= len(prices):
                return 0

            if not bought:
                a = dp(True, i+1) - prices[i]
                b = dp(bought, i+1)
                return max(a, b)

            a =  dp(False, i+1) + prices[i] - fee
            b = dp(bought, i+1)
            return max(a, b)

        return dp(False,0)