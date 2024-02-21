class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(idx, flag):
            if idx == len(nums) - 1:
                return 0 if flag else nums[idx]

            if idx == len(nums) - 2:
                return nums[idx] if flag else max(nums[idx], nums[idx+1])

            if (idx, flag) not in memo:
                memo[(idx, flag)] = max(nums[idx] + dp(idx+2, flag), dp(idx+1, flag))
            return memo[(idx, flag)]

        if len(nums) < 3:
            return max(nums)
        return max(nums[0] + dp(2, True), dp(1, False))