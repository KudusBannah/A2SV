class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        distances = [-1] * n

        def bfs():
            queue = [(0, 0)]
            heapify(queue)
            visited = set()

            while len(queue):
                cost, curr = heappop(queue)

                if curr in visited:
                    continue

                visited.add(curr)
                distances[curr] = cost

                for n, c in graph[curr]:
                    if n not in visited:
                        heappush(queue, (cost+c, n))
        

        @cache
        def dp(curr, cost):
            if curr == 0:
                return 1

            ways = 0
            for n,c in graph[curr]:
                if distances[n] + cost + c == distances[-1]:
                    ways += dp(n, cost + c)
            return ways
            
            
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        bfs()
        return dp(n-1, 0) % (10**9+ 7)
