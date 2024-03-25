class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        def is_valid(curr):
            rem = 0
            for i in range(len(nums)-1, -1, -1):
                if nums[i]+rem > curr:
                    rem = (nums[i]+rem) - curr
                else:
                    rem = 0
            return rem == 0
            

        l, r = 0, max(nums)
        best = r
        while l <= r:
            mid = (l+r)//2

            if is_valid(mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1

        return best