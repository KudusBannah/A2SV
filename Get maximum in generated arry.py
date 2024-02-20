class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [-1] * (n + 1)

        def dp(i):
            if nums[i] != -1:
                return nums[i]

            if i < 2:
                nums[i] = i
                return nums[i]

            if i % 2 == 0:
                nums[i] = dp(i//2)
                return nums[i]

            nums[i] = dp(i//2) + dp(i//2 + 1)
            return nums[i]

        for i in range(n, -1, -1):
            dp(i)

        return max(nums)

        