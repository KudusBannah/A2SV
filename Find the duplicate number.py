class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            if nums[i]-1 != i:
                correct = nums[i] - 1
                if nums[correct] ==  nums[i]:
                    return nums[i] 
                else:
                    nums[correct], nums[i] = nums[i], nums[correct]
            else:
                i += 1