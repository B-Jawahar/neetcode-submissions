import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-i for i in stones]
        heapq.heapify(heap)
        print(len(heap))
        while len(heap)>1:
            fmax=heapq.heappop(heap)
            smax=heapq.heappop(heap)
            neww=smax-fmax
            if neww>0:
                heapq.heappush(heap,-neww)
        if len(heap)==1:
            return -heap[0]
        return 0