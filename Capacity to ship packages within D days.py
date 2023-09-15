class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_carry_within_days(ship_weight):
            total_days = 0
            i = 0
            while i < len(weights):
                curr_weight, j = 0, i
                if weights[j] > ship_weight: return False
                while j < len(weights) and (curr_weight + weights[j] <= ship_weight):
                    curr_weight += weights[j]
                    j += 1
                total_days += 1
                i = j    
            return total_days <= days
        
        l, r = 0, sum(weights)
        best = r
        while l <= r:
            mid = l + (r-l)//2
            ans = can_carry_within_days(mid)
            if ans:
                r = mid - 1
                best = mid
            else:
                l = mid + 1
        return best