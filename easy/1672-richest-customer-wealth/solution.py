class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max = 0 
        for row in range(len(accounts)): 
            curr = 0 
            for col in range(len(accounts[row])):
                curr += accounts[row][col]
            if curr > max: 
                max = curr
        
        return max
        