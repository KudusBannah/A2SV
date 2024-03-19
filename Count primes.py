class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
            
        arr = [True] * (n)
        arr[0], arr[1] = False, False

        for i in range(2, int(math.sqrt(n))+1):
            if not arr[i]:
                continue
            j = i ** 2
            while j < n:
                arr[j] = False
                j += i
        return arr.count(True)
        