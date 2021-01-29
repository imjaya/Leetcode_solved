# two approaches
# DP TOP DOWN APPROACH 

class Solution:
    def dp(self,A,B,i,j,dp):
        global ans
        if dp[i][j] != -1:
            return dp[i][j]

        if i == 0 and j == 0:
            ans = 1
        elif j == 0:
            ans = 1

        elif i == 0:
            ans = 0

        elif A[i-1] == B[j-1]:
            ans = self.dp(A,B,i-1,j-1,dp) + self.dp(A,B, i-1,j,dp)
        else:
            ans =  self.dp(A,B,i-1,j,dp)

        dp[i][j] = ans
        return ans
    
    def numDistinct(self, A: str, B: str) -> int:
        m = len(A)
        n = len(B)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        return self.dp(A,B,m,n,dp)


     # DP BOTTOM UP APPROACH
    class Solution:
    def numDistinct(self, A: str, B: str) -> int:
        m = len(A)
        n = len(B)
        if m == 0 or n == 0: return 0
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1

                elif j == 0:
                    dp[i][j] = 1

                elif A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]