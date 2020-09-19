int solve(string& s,string& t,int i,int j,vector<vector<int>>&dp)
{
    if(j==-1)return 1;
    if(i<0)return 0;
    if(dp[i][j]!=-1)return dp[i][j];
    int res=0;
    if(s[i]==t[j])
    {
        res=res+solve(s,t,i-1,j-1,dp);
    }
    res=res+solve(s,t,i-1,j,dp);
    return dp[i][j]=res;
    
}
class Solution {
public:
    int numDistinct(string s, string t) {
     int n=s.length();
        int m=t.length();
        if(m>n)return 0;
        vector<vector<int>>dp(n,vector<int>(m,-1));
        return solve(s,t,n-1,m-1,dp);
    }
};