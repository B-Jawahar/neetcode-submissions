import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.k=k
        n=len(nums)
        if n<=k:
            self.heap=nums
            heapq.heapify(self.heap)
            self.count=n
        else:
            nums=nums[n-k:]
            self.heap=nums
            heapq.heapify(self.heap)
            self.count=k+1
        print(self.heap)

    def add(self, val: int) -> int:
        print(self.count)
        if self.count<self.k:
            heapq.heappush(self.heap,val)
            self.count+=1
            return self.heap[0]
        elif self.count==self.k:
            self.count+=1
            if val<=self.heap[0]:
                return self.heap[0]
            heapq.heappushpop(self.heap,val)
            return self.heap[0]
        else:
            if val<=self.heap[0]:
                return self.heap[0]
            heapq.heappushpop(self.heap,val)
            return self.heap[0]
