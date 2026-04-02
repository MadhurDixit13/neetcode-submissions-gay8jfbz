"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_list = sorted(intervals, key=lambda x:x.start)
        for i in range(1, len(intervals)):
            if (sorted_list[i].start < sorted_list[i-1].end):
                return False
            
        return True