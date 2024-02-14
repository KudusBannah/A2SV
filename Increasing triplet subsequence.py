class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num, second_num = float("INF"), float("INF")

        for i in range(len(nums)):
            if nums[i] <= first_num:
                first_num = nums[i]
            elif nums[i] <= second_num:
                second_num = nums[i]
            else:
                return True
        
        return False