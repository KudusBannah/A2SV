class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        memo = {}

        def dfs(curr, visited):
            if curr in memo:
                return memo[curr]
            if adj_list[curr] == []:
                return True
            if curr in visited:
                return False

            visited.add(curr)

            for neighbour in adj_list[curr]:
                if not dfs(neighbour, visited):
                    memo[curr] = False
                    return memo[curr]
            
            visited.remove(curr)
            memo[curr] = True
            return memo[curr]

        adj_list = defaultdict(list)
        for i in range(len(graph)):
            adj_list[i].extend(graph[i])

        output = []
        for i in range(len(graph)):
            if dfs(i, set()):
                output.append(i)
        return output