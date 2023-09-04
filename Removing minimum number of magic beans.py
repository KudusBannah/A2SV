class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        sum_ = sum(beans)
        prefix_length = [0] * (len(beans)+1)
        for i in range(1, len(prefix_length)):
            prefix_length[i] = prefix_length[i-1] + 1

        min_ = float('inf')
        for i in range(len(beans)):
            remain = (prefix_length[-1] - prefix_length[i]) * beans[i]
            min_ = min(min_, sum_ - remain)

        return min_