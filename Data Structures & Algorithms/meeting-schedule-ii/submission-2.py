"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals==[]:
            return 0
        maxint=max(i.end for i in intervals)
        print(maxint)
        count=[0]*maxint
        for i in intervals:
            for j in range(i.start,i.end):
                #print(j)
                count[j]+=1
        return max(count)

