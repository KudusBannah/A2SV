class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1*stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            a = abs(heappop(heap))
            b = abs(heappop(heap))
            if a != b:
                heappush(heap, -1*abs(a-b))
        return abs(heap[0]) if heap else 0
