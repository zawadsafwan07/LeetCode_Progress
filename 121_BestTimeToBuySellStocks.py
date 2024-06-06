# LeetCode Problem 121 Best time to buy sell stocks
# Date : June 4th 2024
# Abrar Zawad Safwan

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest_price = prices[0]
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            result = max(result, price - lowest_price)
        return result

