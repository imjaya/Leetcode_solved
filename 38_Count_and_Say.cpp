class Solution {
public:
    string next(string & a)
    {
        string n="";
        char ch=a[0];int c=1;
        for(int i=1;i<a.size();i++)
        {
            if(a[i]==ch)c++;
            else{
                n+=c+'0';
                n+=ch;
                ch=a[i];c=1;
            }
        }
        n+=c+'0';n+=ch;
        return n;
    }
    string countAndSay(int n) {
        string ans="1";
        for(int i=0;i<n-1;i++)
            ans=next(ans);
        return ans;
    }
};