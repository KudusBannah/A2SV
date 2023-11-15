class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = defaultdict(int)
        for word in words:
            words_count[word] += 1

        heap = [(-1*words_count[word], word) for word in words_count]
        heapify(heap)
        output = []
        for i in range(k):
            output.append(heappop(heap)[1])
        return output
