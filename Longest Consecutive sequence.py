class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        max_sequence = 0

        for num in nums:
            if not (num - 1) in checker:
                length = 1
                while (num+length) in checker:
                    length += 1
                max_sequence = max(max_sequence, length)
        return max_sequence