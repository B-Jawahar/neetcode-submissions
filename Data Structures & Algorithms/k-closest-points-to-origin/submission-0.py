import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[(math.sqrt(i[0]*i[0]+i[1]*i[1]),i) for i in points]
        heapq.heapify(heap)
        result=[]
        while k>0:
            k-=1
            result.append(heapq.heappop(heap)[1])
        return result

