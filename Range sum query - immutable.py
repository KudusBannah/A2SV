class NumArray:

    def __init__(self, nums: List[int]):
        self.p_sum = [0] * (len(nums))
        self.p_sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.p_sum[i] = nums[i] + self.p_sum[i-1]


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.p_sum[right]
        return self.p_sum[right] - self.p_sum[left-1]