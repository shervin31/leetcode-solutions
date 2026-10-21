class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = float("inf")
        max_profit = 0 
        
        i = 0
        while i < len(prices): 
            if prices[i] < min: 
                min = prices[i] 
            profit = prices[i] - min
            if profit > max_profit: 
                max_profit = profit 
            i += 1
        return max_profit 
        