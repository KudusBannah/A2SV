class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a, set_b = set(), set()
        counter = 0
        prefix_arr = [0] * len(A)
        for i in range(len(A)):
            a, b = A[i], B[i]
            if a == b:
                counter += 1
            elif (a in set_b) and (b in set_a):
                counter += 2
            elif (a in set_b):
                counter += 1
            elif (b in set_a):
                counter += 1
            prefix_arr[i] = counter
            set_a.add(a)
            set_b.add(b)
        return prefix_arr