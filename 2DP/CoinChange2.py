class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}

        def dfs(coin_ind,curr_amount):
            if curr_amount == 0:
                return 1

            if coin_ind >= len(coins):
                return 0
            
            if (coin_ind,curr_amount) in memo:
                return memo[(coin_ind,curr_amount)]

            res = 0
            if curr_amount >= coins[coin_ind]:
                res = dfs(coin_ind,curr_amount - coins[coin_ind])    # Continue with this current calculation
                res += dfs(coin_ind + 1, curr_amount)                  # To avoid duplication of previous coin i
            memo[(coin_ind,curr_amount)] = res
            return res


        return dfs(0, amount)