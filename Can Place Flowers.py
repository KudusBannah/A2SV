class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        if N == 1:
            if flowerbed[0] == 0: n -= 1
            return n <= 0
        for i in range(N):
            if not flowerbed[i]:
                if (i == 0 and not flowerbed[i+1]) or (i == N-1 and not flowerbed[i-1]):
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
