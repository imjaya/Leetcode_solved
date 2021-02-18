class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        stack<pair<int, int>> st;
        vector<int> ans;
        for(int i=T.size()-1;i>=0;i--){
            while(!st.empty() && st.top().first <= T[i]) st.pop();
            if(st.empty()) ans.push_back(0);
            else{
                ans.push_back(st.top().second - i);
            }
            st.push({T[i], i});
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};