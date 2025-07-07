class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy
        max_profit = 0

        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right  # Move buy day to the cheaper price

        return max_profit