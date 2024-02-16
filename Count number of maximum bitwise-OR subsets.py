class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        def form_subsets(curr_subset, idx):
            nonlocal max_, count
            if idx >= len(nums):
                # check for the value of the bitwise
                temp = 0
                for num in curr_subset:
                    temp |= num

                if temp > max_:
                    max_ = temp
                    count = 1
                elif temp == max_:
                    count += 1
                return

            curr_subset.append(nums[idx])
            form_subsets(curr_subset, idx + 1)

            curr_subset.pop()
            form_subsets(curr_subset, idx + 1)


        max_, count = 0, 0
        form_subsets([], 0)
        return count