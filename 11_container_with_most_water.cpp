class Solution {
public:
    int maxArea(vector<int>& v) {
        if(v.size()==2)
            return v[0]<=v[1]?v[0]:v[1];
        int start=0, end=v.size()-1;
       int ans=0;
        while(start<end)
        {
            ans=max(ans,(min(v[start],v[end])*(end-start)));
            if(v[start]<=v[end]||v[start+1]>=v[start]+1)
                start++;
            else if(v[end]<=v[start]||v[end-1]>=v[end]+1)
                end--;
            
        }
        
        return ans;
    }
};