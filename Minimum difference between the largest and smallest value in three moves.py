class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) <= 4:
            return 0
            
        # We have 4 combinations at each point
        min_arr = []
        min_arr.append(nums[-1]-nums[3])
        min_arr.append(nums[-4]-nums[0])
        min_arr.append(nums[-2]-nums[2])
        min_arr.append(nums[-3]-nums[1])
         
        return min(min_arr)