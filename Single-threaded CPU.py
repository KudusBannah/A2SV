class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        my_dict = defaultdict(list)
        for i in range(len(tasks)):
            my_dict[tasks[i][0]].append([tasks[i][1], i])
        
        sorted_keys = sorted(my_dict.keys())
        sorted_tasks = []
        for key in sorted_keys:
            sorted_tasks.extend([[key, el] for el in my_dict[key]])

        heap = []
        heapify(heap)
        res = []
        curr, i = 1, 0
        while i < len(sorted_tasks):
            while i < len(sorted_tasks) and sorted_tasks[i][0] <= curr:
                item = sorted_tasks[i]
                heappush(heap, (item[1][0], item[1][1]))
                i += 1

            if heap:
                popped = heappop(heap)
                res.append(popped[1])
                curr += popped[0]
            else:
                curr = sorted_tasks[i][0]

        while heap:
            popped = heappop(heap)
            res.append(popped[1])
        return res