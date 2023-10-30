#Total profit here is kinda determining each consecutive valleys and peaks and summing up total profit.
# TC: O(N), SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_valley = 100000
        total_profit = 0

        for price in prices:
            if price < cur_valley:
                cur_valley = price
            elif price > cur_valley:
                total_profit += price - cur_valley
                cur_valley = price
        return total_profit
        