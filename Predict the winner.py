class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def dp(l, r, p1_turn):
            if l == r:
                return nums[l] if p1_turn else -nums[l]

            if p1_turn:
                a = nums[l] + dp(l+1, r, not p1_turn)
                b = nums[r] + dp(l, r-1, not p1_turn)
                return max(a, b)
            
            a = -nums[l] + dp(l+1, r, not p1_turn)
            b = -nums[r] + dp(l, r-1, not p1_turn)
            return min(a, b)

        return dp(0, len(nums)-1, True) >= 0