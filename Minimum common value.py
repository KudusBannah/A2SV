class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)

        common = nums1 & nums2
        if common:
            return min(common)
        return -1