class Solution {
public:
    vector<vector<int>> v;
    bool isMatch(string s, string p) {
    for(int i=0;i<=s.length();i++)
    {
        vector<int> u;
        for(int j=0;j<=p.length();j++)
        {
            u.push_back(-1);
        }
        v.push_back(u);
    }
        helper(s, p,0,0); 
        return v[0][0];
    }
    bool helper(string s, string p,int i,int j)
    {
        if (j==p.length()){
                v[i][j]=i==s.length();
                return (i==s.length());
        } 
        if(v[i][j]<0)
        {
            bool first_match = (i<s.length() && (p[j]==s[i] || 
                                                 p[j]== '.'));
            if (j+1<p.length() && p[j+1] == '*'){
            v[i][j]= ((helper(s,p,i,j+2)) ||
                    (first_match && helper(s, p,i+1,j)));
            } else {
                v[i][j]= first_match && helper(s,p,i+1,j+1);
            } 
        }
    
        return v[i][j];
       
    }
    
};