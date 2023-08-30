class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        my_dict = {0:1}
        count = 0
        for num in nums:
            complement = num % k
            if complement in my_dict:
                count += my_dict[complement]
                my_dict[complement] += 1
            else: my_dict[complement] = 1
        return count