class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(sum_, idx):
            if idx == len(nums):
                return int(sum_ == target)

            if (sum_, idx) not in memo:
                a = dp(sum_ + nums[idx], idx + 1)
                b = dp(sum_ - nums[idx], idx + 1)
                memo[(sum_, idx)] = a + b

            return memo[(sum_, idx)]
        
        return dp(0, 0)