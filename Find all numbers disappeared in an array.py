class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if i != nums[i]-1:
                correct = nums[i] - 1
                if nums[correct] == nums[i]:
                    i += 1
                else:
                    nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        print(nums)
        output = []
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                output.append(i+1)
        return output