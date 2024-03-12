class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        def bfs(start):
            queue = [(0, start)]
            heapify(queue)
            visited = set()
            
            best = 0
            while len(queue):
                cost, curr = heappop(queue)
                visited.add(curr)

                if len(visited) == n:
                    return cost
                
                for neigh in adj_list[curr]:
                    neigh_cost = neigh[0] + cost
                    neigh_node = neigh[1]

                    if (neigh_node) not in visited:
                        heappush(queue, (neigh_cost, neigh_node))

            return -1

        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((w, v))
        
        return bfs(k)

        


        
