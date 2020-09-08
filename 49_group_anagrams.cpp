class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<int>> m;
        string s;
        int i;
        for(i=0;i<strs.size();i++)
        {
            s=strs[i];
            sort(s.begin(),s.end());
            m[s].push_back(i);
        }
        vector<vector<string>> ans(m.size());
        i=0;
        for(auto str:m)
        {
            for(auto x:str.second)
            {
                ans[i].push_back(strs[x]);
            }
            i++;
        }
        return ans;
    }
};