class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=0
        result=[intervals[0]]
        for start,end in intervals[1:]:
            if start<result[-1][1]:
                count+=1
            else:
                result.append([start,end])
        return len(intervals)-len(result)

                