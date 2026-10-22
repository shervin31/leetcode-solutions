class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = float('inf')
        max_prof = 0 
        for price in prices:
            if price < min: 
                min = price
            if price - min > max_prof: 
                max_prof = price - min
            
        return max_prof
            
        
        