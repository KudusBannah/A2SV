class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        memo = {}
        def dp(i, j):
            if i >= len(matrix):
                return 0

            # Three ways to go
            if (i, j) not in memo:
                l = dp(i+1, j-1) if (j-1) >= 0 else float("inf")
                b = dp(i+1, j)
                r = dp(i+1, j+1) if (j+1) < len(matrix[0]) else float("inf")
                memo[(i,j)] = min(l, r, b) + matrix[i][j]
            return memo[(i, j)]

        min_ = float("INF")
        for i in range(len(matrix[0])):
            min_ = min(min_, dp(0, i))
        return min_