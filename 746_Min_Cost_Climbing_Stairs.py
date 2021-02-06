class Solution(object):
    def minCostClimbingStairs(self, cost):
        f1 = cost[0] 
        f2 = cost[1]
        for i in range(2,len(cost)):
            f1, f2 = f2,cost[i] + min(f1, f2)
        return min(f1, f2)