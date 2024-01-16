class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        output = set()
        while i < len(nums):
            if i != nums[i]-1:
                correct = nums[i] - 1
                if nums[correct] == nums[i]:
                    output.add(nums[i])
                    i += 1
                else:
                    nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        return output