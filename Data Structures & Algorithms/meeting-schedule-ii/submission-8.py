import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)
        
        heap = []  # stores end times
        
        for interval in intervals:
            # free a room
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)
            
            # allocate room
            heapq.heappush(heap, interval.end)
        
        return len(heap)