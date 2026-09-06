class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            profit_if_sell_today = prices[i]-min_price
            max_profit = max(max_profit,profit_if_sell_today)

        return max_profit