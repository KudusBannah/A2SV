class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a_list = defaultdict(list)
        for edge in edges:
            a_list[edge[0]].append(edge[1])
            a_list[edge[1]].append(edge[0])

        def dfs(vertex, visited):
            if vertex in visited:
                return
            if len(a_list[vertex]) == len(a_list) - 1:
                return vertex

            visited.add(vertex)
            for n in a_list[vertex]:
                ans = dfs(n, visited)
                if ans: return ans
            return

        return dfs(edges[0][0], set())