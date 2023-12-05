class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            nonlocal visited
            if node in visited:
                return
            visited.add(node)
            for connected_city in graph[node]:
                dfs(connected_city)


        graph = defaultdict(set)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i+1].add(j+1)
                    graph[j+1].add(i+1)
        
        province_count = 0
        visited = set()
        for city in range(1, n+1):
            if city not in visited:
                dfs(city)
                province_count += 1
        return province_count