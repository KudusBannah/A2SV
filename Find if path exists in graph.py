class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        a_list = defaultdict(list)
        for edge in edges:
            a_list[edge[0]].append(edge[1])
            a_list[edge[1]].append(edge[0])

        print(a_list)
        def dfs(node, visited):
            if node == destination:
                return True
            
            visited.add(node)
            for neighbour in a_list[node]:
                if neighbour not in visited:
                    if dfs(neighbour, visited): return True
            return False