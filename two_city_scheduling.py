class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [(cost[1]-cost[0], i) for i, cost in (enumerate(costs))]
        diff.sort()

        res = 0
        for i in range(len(costs)):
            curr = diff[i]
            if i < len(costs)//2:
                res += costs[curr[1]][1]
            else:
                res += costs[curr[1]][0]

        return res