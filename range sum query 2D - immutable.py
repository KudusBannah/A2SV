class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.p_sum = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.p_sum[i+1][j+1] = matrix[i][j] + self.p_sum[i+1][j] + self.p_sum[i][j+1] - self.p_sum[i][j]     

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = self.p_sum[row2+1][col2+1] - self.p_sum[row1][col2+1] - self.p_sum[row2+1][col1] + self.p_sum[row1][col1] 
        return sum_