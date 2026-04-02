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
        int start=-1;
        int end=-1;
        int lowestEnd = numeric_limits<int>::max();
        int count = 0;
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        vector<int> starts(intervals.size(), 0);
        // for(auto& i:intervals){
        //     // starts.push_back(i.start);
        //     ends.push_back(i.end);
        // }
        // sort(ends.begin(), ends.end(),greater<>());
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
            // start = i.start;
            // end= i.end;
        }
        return count;
    }
};
