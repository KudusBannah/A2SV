class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        postfix_product = [1] * len(nums)
        prefix_product[1], postfix_product[-2] = nums[0], nums[-1]

        for i in range(1, len(nums)-1):
            prefix_product[i+1] = prefix_product[i] * nums[i]

        for i in range(len(nums)-2, 0, -1):
            postfix_product[i-1] = postfix_product[i] * nums[i]

        for i in range(len(nums)):
            nums[i] = postfix_product[i] * prefix_product[i]

        return nums
