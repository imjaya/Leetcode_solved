   int minCostClimbingStairs(vector<int>& c) {
        int n=c.size();
        int dp[n+2];
        
        dp[0]=c[0];
        dp[1]=c[1];
        
        for(int i=2;i<n;i++){
            dp[i]=min(c[i]+dp[i-1],c[i]+dp[i-2]);
        }
        
        dp[n]=min(dp[n-1],dp[n-2]);
        
        return dp[n];
    }