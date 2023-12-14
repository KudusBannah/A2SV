class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        valid_moves = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1), (3, 1), (3, -1)]
        
        queue = deque([["0000", 0]])
        visited = set(deadends)
        
        while queue:
            curr, level = queue.popleft()

            if curr in visited:
                continue
            visited.add(curr)

            if curr == target:
                return level

            for i, val in valid_moves:
                x = (int(curr[i]) + val) % 10
                new = curr[:i] + str(x) + curr[i+1:]

                if new not in visited:
                    queue.append([new, level + 1])

        return -1
