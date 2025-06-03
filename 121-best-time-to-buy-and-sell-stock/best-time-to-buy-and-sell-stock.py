class Solution(object):
    def maxProfit(self, prices): 
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price - min_price > max_profit:
                max_profit = price- min_price
            if price < min_price:
                min_price = price
        return max_profit