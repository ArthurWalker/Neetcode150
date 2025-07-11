"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key= lambda x: x.start)
        i = 1
        n = len(intervals)
        temp = []
        for inter in intervals:
            if not temp or temp[-1].end <= inter.start:
                temp.append(inter)
            else:
                return False
        return True