class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        defined_paths = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(row, col):
            nonlocal visited
            if (row, col) in visited or grid[row][col] == "0":
                return

            visited.add((row, col))
            for path in defined_paths:
                r, c = row + path[0], col + path[1]
                if (r>=0 and r<len(grid)) and (c>=0 and c<len(grid[0])):
                    dfs(r, c)
                
            
        
        count, visited = 0, set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1") and ((i, j) not in visited):
                    dfs(i, j)
                    count += 1
        return count