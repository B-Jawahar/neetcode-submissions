class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[0]*26
        for i in tasks:
            count[ord(i)-ord('A')]+=1
        maxc=max(count)
        maxcount=0
        for i in count:
            if i==maxc:
                maxcount+=1
            
        return max(len(tasks),(maxc-1)*(n+1)+maxcount)
