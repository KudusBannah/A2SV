class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        l, r = 0, N - 1

        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            if (N - mid) <= citations[mid]:
                ans = N - mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
