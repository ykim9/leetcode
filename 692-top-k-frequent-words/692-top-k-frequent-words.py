class Solution:
    import heapq
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        counter = collections.Counter(words)
        for word in counter:
            heapq.heappush(heap, (-counter[word], word))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
        