class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int strNumbers = strs.size();
        int j = 0;
        if (strNumbers==0) {
            return "";
        } else if (strNumbers==1) {
            return strs[0];
        } else {
            int firstWordLen = strs[0].length();
            int i = 1;
            while (strs[0][j]==strs[i][j] && strs[0][j]!='\0') {
                i = ( i + 1) % strNumbers;
                if (i==0) {
                    j++;
                    i++;
                }
            }
        }
        return strs[0].substr(0, j);
    }
};