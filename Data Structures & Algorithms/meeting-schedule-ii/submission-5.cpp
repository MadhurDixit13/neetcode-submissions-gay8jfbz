/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */
void sortIntervals(std::vector<Interval>& intervals) {
    std::sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) {
        return a.start < b.start;
    });
}
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int highestStart = 0;
        int lowestEnd = numeric_limits<int>::max();
        int count = 0;
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        sortIntervals(intervals);
        for(auto& i:intervals){
            if(i.start < lowestEnd){
                count++;
            }
            if(i.start==lowestEnd){
                pq.pop();
                lowestEnd=pq.top();
            }
            pq.push(i.end);
            if(highestStart<i.start){highestStart = i.start;}
            if(lowestEnd>i.end){lowestEnd = i.end;}
            cout<<lowestEnd<<endl;
        }
        return count;
    }
};
