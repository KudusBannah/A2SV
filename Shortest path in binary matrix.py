class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        defined_paths = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        queue = deque([[0, 0, 1]])
        visited = set()
        ans = -1

        while queue:
            cur_x, cur_y, level = queue.popleft()
            if (cur_x, cur_y) in visited:
                continue
                
            visited.add((cur_x, cur_y))

            if (cur_x == len(grid) - 1) and (cur_y == len(grid[0])-1):
                ans = level
                break

            for path in defined_paths:
                new_x = cur_x + path[0]
                new_y = cur_y + path[1]

                if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                    if (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                        queue.append([new_x, new_y, level+1])
        return ans
                    




        