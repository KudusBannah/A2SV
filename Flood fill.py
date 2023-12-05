class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        defined_paths = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(r, c, parent_color):
            nonlocal visited
            if (r, c) in visited or image[r][c] != parent_color:
                return

            visited.add((r, c))
            for path in defined_paths:
                new_r, new_c = r + path[0], c + path[1]
                if new_r >= 0 and new_r < len(image) and new_c >= 0 and new_c < len(image[0]):
                    dfs(new_r, new_c, parent_color)
            
            image[r][c] = color
            print(r, c)
        
        visited = set()
        dfs(sr, sc, image[sr][sc])
        return image
        