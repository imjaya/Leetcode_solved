class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> hash;
        map<int,vector<int>, greater<int>> map;
        vector<int> res;
        
        int n=nums.size();
        for(int i=0; i<n; i++)
            hash[nums[i]]++;
        
        for(auto i=hash.begin(); i!=hash.end(); i++)
        {
            map[i->second].push_back(i->first);
        }
        
        for(auto i=map.begin(); i!=map.end() && k>0; i++)
        {
            // for(int j=0; j<(i->second).size(); j++)
            //     cout<<(i->second)[j];
            // cout<<endl;
            if((i->second).size()<=k)
            {
                res.insert(res.begin(), (i->second).begin(), (i->second).end());
                k-=(i->second).size();
            }
            else
            {
                res.insert(res.begin(), (i->second).begin(), (i->second).begin()+k);
                break;
            }
        }
        
        return res;
    }
};