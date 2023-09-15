class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish_bananas(num):
            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile/num)
            return total_hours <= h
        
        l, r = 1,  max(piles)
        k = r - 1
        while l <= r:
            mid = (l+r)//2
            ans = can_finish_bananas(mid)
            if ans:
                r = mid - 1
                k = mid
            else:
                l = mid + 1
        return k