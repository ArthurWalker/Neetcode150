class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Every decision, we can choose to (buy or cooldown) or (sell or cooldown).
        # However, after a sell, there must be a cooldown

        buying = True
        memo = {}

        def dfs(day,buying):
            if day >= len(prices):
                return 0
            if (day,buying) in memo:
                return memo[(day,buying)]
            cooldown = dfs(day+1,buying)
            if buying:
                buy = dfs(day+1,not buying)-prices[day]
                memo[(day,buying)] = max(buy,cooldown)
            else:
                sell = dfs(day+2,not buying)+prices[day]
                memo[(day,buying)] = max(sell,cooldown)
            return memo[(day,buying)] 

        return dfs(0,True)