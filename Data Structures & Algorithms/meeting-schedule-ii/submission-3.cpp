#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        if (intervals.empty()) return 0;

        // Step 1: Sort intervals based on start time
        sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) {
            return a.start < b.start;
        });

        // Min-heap to store end times of meetings
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (const auto& meeting : intervals) {
            // Step 2: If the earliest meeting in the heap has ended, remove it
            if (!minHeap.empty() && minHeap.top() <= meeting.start) {
                minHeap.pop();
            }

            // Step 3: Push the current meeting's end time into the heap
            minHeap.push(meeting.end);
        }

        // Step 4: The heap size represents the number of rooms needed
        return minHeap.size();
    }
};
