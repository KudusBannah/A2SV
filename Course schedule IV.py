class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[float("inf")]*numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            dp[u][v] = 1

        for i in range(numCourses):
            dp[i][i] = 0
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
        query_res = []
        for u, v in queries:
            if dp[u][v] == float("inf"):
                query_res.append(False)
            else:
                query_res.append(True)
        
        return query_res
        