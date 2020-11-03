class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        stable_sort(logs.begin(),logs.end(), [](const string& a, const string& b) -> bool {
            int i = a.find(' '), j = b.find(' ');
            
            if (!isdigit(a[i+1]) && !isdigit(b[j+1])) {
                string s1 = a.substr(i+1), s2 = b.substr(j+1);
                if(s1 == s2) return a.compare(b) < 0;
                return s1.compare(s2) < 0;
            }
            
            return !isdigit(a[i+1]);
        });
        
        return logs;
    }
};