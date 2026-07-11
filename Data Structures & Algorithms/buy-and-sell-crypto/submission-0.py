class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = profit = 0
        left = 0
        buy = prices[left]
        for right in range(1,len(prices)):
            if buy > prices[right]:
                left = right
                buy = prices[left]
            profit = prices[right] - buy
            max_profit = max(profit,max_profit)
        return max_profit
