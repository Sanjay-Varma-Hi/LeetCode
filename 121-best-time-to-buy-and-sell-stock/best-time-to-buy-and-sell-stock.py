class Solution(object):
    def maxProfit(self, prices): 
        l= 0
        max_profit = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit>max_profit:
                    max_profit = profit
            else:
                l=r
        return max_profit