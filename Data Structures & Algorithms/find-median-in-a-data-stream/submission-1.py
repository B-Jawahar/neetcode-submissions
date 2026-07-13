import heapq
class MedianFinder:

    def __init__(self):
        self.heap=[]
        heapq.heapify(self.heap)
        self.l=0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap,num)
        self.l+=1

    def findMedian(self) -> float:
        pp=[]
        print(self.heap)
        if self.l%2!=0:
            i=(self.l//2)
            for _ in range(i):
                print("heap",self.heap)
                pp.append(heapq.heappop(self.heap))
                print("pp",pp)
            mid=self.heap[0]
            for i in pp:
                heapq.heappush(self.heap,i)
            return mid/1
        else:
            i=(self.l//2)
            print(i)
            for _ in range(i-1):
                pp.append(heapq.heappop(self.heap))
            mid1=self.heap[0]
            pp.append(heapq.heappop(self.heap))
            mid2=self.heap[0]
            for i in pp:
                heapq.heappush(self.heap,i)
            return (mid1+mid2)/2

        