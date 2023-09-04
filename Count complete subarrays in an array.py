class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        right ,left = 0,0
        ans = 0 
        nums_set = set(nums)
        sub_arr_set = set()
        cur_sub_cnt = 0
        f_dict = defaultdict(int)

        for right in range(len(nums)):
            sub_arr_set.add(nums[right])
            f_dict[nums[right]] += 1
                
            while sub_arr_set == nums_set:
                sub_arr_set.remove(nums[left])
                if f_dict[nums[left]] > 1:
                    f_dict[nums[left]] -= 1
                    sub_arr_set.add(nums[left])
                else:
                    f_dict[nums[left]] -= 1
                left += 1
                cur_sub_cnt += 1
                
            ans += cur_sub_cnt
            
        return ans