class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = sum(nums[:k])
        sum_ = 0
        distint_dict = defaultdict(int)
        n = k
        for num in nums[:k]:
            distint_dict[num] += 1
            if distint_dict[num] != 1:
                n-= 1
        if n == k:
            sum_ = curr_sum

        for l in range(0, len(nums) - k):
            r = l + k
            curr_sum += nums[r]
            curr_sum -= nums[l]

            distint_dict[nums[l]] -= 1
            if distint_dict[nums[l]] == 0:
                n -= 1
            
            distint_dict[nums[r]] += 1
            if distint_dict[nums[r]] == 1:
                n += 1

            if n == k:
                sum_ = max(sum_, curr_sum)
        return sum_