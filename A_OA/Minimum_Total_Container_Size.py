class Solution:
    def minDifficulty(self, P: List[int], d: int) -> int:
        
             
        N_item = len(P)
        DP = [ [None]*N_item for _ in range(d)]
        DP[0][0] = P[0]
        for i in range(1,N_item-(d-1)):
            DP[0][i] = max(P[0:i+1])

        for day in range(1,d):
            items_inder_consideration = N_item-(d-(day+1))
            for item in range(day,items_inder_consideration):
                DP[day][item] = float("inf")
                for i in range(day,item+1):
                    val = max(P[i:item+1]) + DP[day-1][i-1]
                    DP[day][item] = min(DP[day][item],val)

        if DP[d-1][N_item-1] == None:
            return -1
        return DP[d-1][N_item-1]