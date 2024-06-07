# LeetCode Problem 122 Rotate Array 
# Date : June 4th 2024
# Abrar Zawad Safwan
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0    #initalize the profit variable

        for i in range(1,len(prices)):
            if (prices[i]>prices[i-1]):
                total_profit+= (prices[i]- prices[i-1])
            
        return total_profit
