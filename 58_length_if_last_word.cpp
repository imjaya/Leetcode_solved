class Solution {
public:
    int lengthOfLastWord(string s) {
        s=" "+s;
        int c=0, i=s.size()-1;
        for( ; i>-1&&!isalpha(s[i]); i--);
        for( ; i>-1&&s[i]!=' '; i--)
            c++;
        return c;
    }
};