import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, s * -1)
        
        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            
            if x < y:
                heapq.heappush(heap, x-y)
            elif x > y:
                heapq.heappush(heap, y-x)
        
        return heap[-1] * -1 if len(heap) else 0