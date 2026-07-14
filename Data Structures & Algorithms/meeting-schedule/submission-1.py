"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals==[]:
            return True
        intervals.sort(key=lambda x:x.start)
        result=[[intervals[0].start,intervals[0].end]]
        for i in intervals[1:]:
            print(result,i.start)
            if result[-1][1]>i.start:
                return False
            else:
                result.append([i.start,i.end])
        return True
            
