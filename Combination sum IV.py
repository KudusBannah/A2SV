class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(cur_sum):
            if cur_sum == target or cur_sum > target:
                return int(cur_sum == target)

            sum_ = 0
            for num in nums:
                sum_ += dp(cur_sum + num)
            return sum_
        
        return dp(0)