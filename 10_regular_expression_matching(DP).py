class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, m + 1):
            if i >= m or p[i] != "*":
                if p[i-1] == "*":
                    dp[i] = dp[i-1]
                else:
                    for j in range(1, n+1):
                        dp[i][j] = dp[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == ".")
            else:
                match, j = p[i-1], 1
				# Handle special case: s = "aab", t = "c*a*b", it removes the c from beginning.
                dp[i][0] = dp[i-1][0] 
                while j < n + 1:
                    if dp[i-1][j-1]:
                        while j < n + 1 and (match == s[j-1] or match == "."):
                            dp[i][j] = True
                            j += 1
                    if j < n + 1: dp[i][j] = dp[i-1][j]
                    j += 1

        return dp[m][n]