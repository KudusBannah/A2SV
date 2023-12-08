class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        found_keys = defaultdict(list)
        for i in range(len(rooms)):
            found_keys[i] = rooms[i]

        visited = set()
        queue = deque([0])
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            for key in found_keys[curr]:
                if key not in visited:
                    queue.append(key)
        return len(visited) == len(rooms)