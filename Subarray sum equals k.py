class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        count = 0
        curr_window = {0:1}
        for num in nums:
            if (num - k) in curr_window:
                count += curr_window[num - k]

            if num in curr_window: curr_window[num] += 1
            else: curr_window[num] = 1
        return count