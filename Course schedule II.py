class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(curr):
            nonlocal visited, path, results, valid
            
            if curr in path:
                valid = False
                return

            if curr in visited:
                return

            visited.add(curr)
            path.add(curr)
            
            for neighbour in adj_list[curr]:
                dfs(neighbour)

            results.append(curr)
            path.remove(curr)
            

        adj_list = defaultdict(list)

        for rel in prerequisites:
            adj_list[rel[0]].append(rel[1])

        visited, path = set(), set()
        valid, results = True, []
        for course in range(numCourses):
            dfs(course)

        return results if valid else []