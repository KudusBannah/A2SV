class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        valid_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        res = [[0]*len(mat[0]) for i in range(len(mat))]
        queue = deque([])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append([(i, j), 0])

        visited = set()

        while queue:
            pos, dist = queue.popleft()

            if mat[pos[0]][pos[1]] == 1:
                if (pos[0], pos[1]) not in visited:
                    res[pos[0]][pos[1]] = dist

            if pos in visited:
                continue
            visited.add(pos)
            
            for move in valid_moves:
                new_x, new_y = pos[0]+move[0], pos[1]+move[1]

                if new_x >= 0 and new_x < len(mat) and new_y >= 0 and new_y < len(mat[0]):
                    queue.append([(new_x, new_y), dist+1])
     
        return res
