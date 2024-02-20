class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i-1]:
                idx = i
                for j in range(i, len(arr)):
                    if arr[j] > arr[idx] and arr[j] < arr[i-1]:
                        idx = j
                arr[i-1], arr[idx] = arr[idx], arr[i-1]
                break

        return arr