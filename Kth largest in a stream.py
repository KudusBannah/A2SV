class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        for i in range(len(nums)-k):
            heappop(self.heap)
        print(self.heap)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappop(self.heap)
            heappush(self.heap, val)
        return self.heap[0]
