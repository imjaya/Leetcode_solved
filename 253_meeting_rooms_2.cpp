// O(NlogN)
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        // O(NlogN)
        sort(intervals.begin(), intervals.end(), 
             [](const vector<int>& interval1, const vector<int>& interval2) {
                return interval1[0] < interval2[0];
        });
        
        // O(NlogR)
        int n = intervals.size();
        priority_queue<int, vector<int>, greater<int>> pq;
        
        for(int i=0; i<n; i++)
        {
            if(!pq.empty() && pq.top() <= intervals[i][0])
            {
                pq.pop();
            }
            pq.push(intervals[i][1]);
        }
        
        return pq.size();
    }
};