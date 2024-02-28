class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        my_dict = {}

        for i in range(len(arr)):
            if (arr[i] - difference) in my_dict:
                my_dict[arr[i]] = my_dict[arr[i] - difference] + 1
            else:
                my_dict[arr[i]] = 1

        return max(my_dict.values())