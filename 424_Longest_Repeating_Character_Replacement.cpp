class Solution {
public:
     int characterReplacement(string s, int k) {
        unordered_map<char,int> map;
        
        int i=0,j=0,ans=0,same=0;
        for(i=0;i<s.size();i++)
        {
            same=max(same,++map[s[i]]);
            while(i-j-same+1>k)
            {
                map[s[j]]--;
                j++;
            }
            ans=max(ans,i-j+1);
        }
        return ans;
    }
};