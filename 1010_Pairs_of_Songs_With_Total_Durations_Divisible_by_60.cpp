class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int count = 0;
        vector<int> s(60, 0);
        for(int i = 0; i < time.size(); i++)
        {
            int w = time[i] % 60;
            if(w == 0) count += s[w];
            else count += s[60 - w];
            s[w]++;
        }
        return count;
    }
};