class Solution {
public:
    bool isSubsequence(string s, string t) {
        int left = 0;
        int right = 0;
        if(s.empty())
            return true;
        while(right<t.length()){
		
            if(t[right]==s[left]){
                left++;
                right++;
			
            if(left>=s.length()){
                return true;
            }
            }
            else
                right++;
        }
        return false;
    }
};