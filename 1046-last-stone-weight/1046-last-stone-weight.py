import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1 and heap[0] != 0:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
        
        return -heap[-1]