class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        def dp(target, idx):
            if target <= 0 or idx >= len(nums):
                return target == 0

            if (target, idx) not in memo:
                memo[(target, idx)] = dp(target-nums[idx], idx + 1) or dp(target, idx + 1)
            return memo[(target, idx)]


        a = sum(nums)
        if sum(nums) % 2 == 1:
            return False
        return dp(a//2, 0)