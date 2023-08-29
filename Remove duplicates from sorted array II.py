class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            j = i + 1
            count = 1
            while j < len(nums) and nums[j] == nums[i]:
                count += 1
                j += 1
            if count > 2: del nums[i:i+count-2]
        return len(nums)