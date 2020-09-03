class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minP=((2**32)-1)
        for i in range(len(prices)):
            if prices[i] < minP:
                minP= prices[i]
                
            if prices[i]-minP > profit:
                profit =prices[i]-minP
                
        return profit
        
        