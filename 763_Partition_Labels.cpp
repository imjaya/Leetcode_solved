class Solution {
public:
    vector<int> partitionLabels(string S) {
        array<int,26> last;
        last.fill(-1);
        
        vector<int> result;
        
        for(int i = 0; i < S.size(); ++i) {
            last[S[i] - 'a'] = i;
        }
        
         int p0 = 0, p1 = 1;
        
        for(int i = 0; i < S.size(); ++i) {
            if(i == p1) {
                result.push_back(p1 - p0);
                p0 = p1;
                p1 = i + 1;
            }
            
            p1 = max(last[S[i] - 'a'] + 1, p1);
        }
        
        result.push_back(p1 - p0);
        
        return result;
    }
};