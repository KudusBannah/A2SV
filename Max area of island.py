class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        defined_paths = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c):
            nonlocal visited
            if (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            area = 0
            for path in defined_paths:
                new_r, new_c = r+path[0], c+path[1]
                if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]):
                    area += dfs(new_r, new_c)
            return area + 1

        visited = set()
        max_ = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_ = max(max_, dfs(i, j))
        return max_
