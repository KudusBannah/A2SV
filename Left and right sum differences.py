class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0] * (len(nums))
        right_sum = [0] * (len(nums))

        for i in range(len(nums)):
            j = len(nums) - (1+i)
            if i == 0:
                left_sum[i] = nums[i]
                right_sum[j] = nums[j]
            else:
                left_sum[i] = left_sum[i-1] + nums[i]
                right_sum[j] = right_sum[j+1] + nums[j]
        for i in range(len(nums)):
            nums[i] = abs(left_sum[i] - right_sum[i])
        return nums