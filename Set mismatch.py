class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i]-1 != i:
                correct = nums[i] - 1

                if nums[i] == nums[correct]:
                    i += 1
                else:
                    nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return [nums[i], i + 1]

        
        