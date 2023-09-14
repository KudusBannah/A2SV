class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        temp = float('inf')
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
                temp = min(temp, nums[mid])
        return temp
