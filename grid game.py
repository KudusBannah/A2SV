class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_row_sum = [0] * (len(grid[0])+2)
        bottom_row_sum = [0] * (len(grid[0])+2)

        for i in range(len(top_row_sum)-2, 0, -1):
            top_row_sum[i] = top_row_sum[i+1] + top_row_sum[i-1]
        
        for i in range(1, len(bottom_row_sum)-1):
            bottom_row_sum[i] = bottom_row_sum[i-1] + bottom_row_sum[i-1]

        result = float('inf')
        for i in range(1, len(top_row_sum)-1):
            robot2 = max(top_row_sum[i+1], bottom_row_sum[i-1])
            print(robot2)
            result = min(robot2, result)
        
        return result 