class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        seq = []

        for num in nums:
            while seq and seq[0][0] < num - 1:
                cur = heappop(seq)
                if cur[1] < 3: return False
            if not seq:
                heappush(seq, [num, 1])
            elif seq[0][0] == num - 1:
                cur = heappop(seq)
                cur[0], cur[1] = num, cur[1] + 1
                heappush(seq, cur)
            else:
                heappush(seq, [num, 1])
        
        for s in seq:
            if s[1] < 3:
                return False
        return True