class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid+1] >= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans