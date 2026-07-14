class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result=[]
        for i in queries:
            count=0
            for start,end in intervals:
                
                if start<=i and end>=i:
                    #print(i,start,end)
                    currcnt=end-start+1
                    if count==0:
                        count=currcnt 
                    else:
                        count=min(currcnt,count)
                    if count==1:
                        #result.append(count)
                        break
            if count!=0:
                result.append(count)
            else:
                result.append(-1)
        return result