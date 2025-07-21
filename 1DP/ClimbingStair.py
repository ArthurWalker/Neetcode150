class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0]*(n+1)
        dp[1],dp[2] = 1,2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
    
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         memo = [-1]*n  # Create flag to say if it passes this
#         def dfs(num):  
#             if num > n:
#                 return 0
#             if num == n:
#                 return 1
#             if memo[num] != -1: # if passing this point
#                 return memo[num] # then dont need to go further and return the result at that position

#             memo[num] = dfs(num+1)+dfs(num+2)
#             return memo[num]
        
#         return dfs(0)