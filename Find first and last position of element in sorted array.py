class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_app, last_app = -1, -1
        # Finding the first appearance of the target
        l, r = 0, (len(nums) - 1)
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                if nums[mid] == target: first_app = mid
        
        # Finding the last appearance of the target
        l, r = 0, (len(nums) - 1)
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                if nums[mid] == target: last_app = mid
        
        return [first_app, last_app]