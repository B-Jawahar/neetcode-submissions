class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        #print(intervals)
        for start,end in intervals[1:]:
            if start<=result[-1][1]:
                if end>=result[-1][1]:
                    result[-1][1]=end
            else:
                result.append([start,end])
        return result