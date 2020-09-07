class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) 
    {
      vector<vector <int>> a;
        int f,e,f2,e2,i=1;
        if(intervals.size()==0)
        {
            return intervals;
        }
        sort(intervals.begin(),intervals.end());
        f=intervals[0][0];
        e=intervals[0][1];
        while(i!=intervals.size())
        {
            f2=intervals[i][0];
            e2=intervals[i][1];
            if(f2<=e)
            {
                e=max(e,e2);
            }
            else
            {
                a.push_back({f,e});
                f=f2;
                e=e2;
            }
            i++;
        }
        a.push_back({f,e});
        return a;
    }
};