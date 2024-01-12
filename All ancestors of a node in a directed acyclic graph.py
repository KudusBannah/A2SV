class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def dfs(curr, visited):
            nonlocal output

            if curr in visited:
                return
            visited.add(curr)

            for neighbour in adj_list[curr]:
                dfs(neighbour, visited)

            output.append(curr)
            return output

        adj_list = defaultdict(list)
        
        for edge in edges:
            adj_list[edge[1]].append(edge[0])

        results = []
        for i in range(n):
            output = []
            visited = set()
            for neighbour in adj_list[i]:
                dfs(neighbour, visited)
            results.append(sorted(output))

        return results