class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        dp = [0]*len(nums) # Generate a DP table to save max values at i

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])

        return dp[-1]
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        memo = [-1]*len(nums)
        def dfs(i):
            if i >=len(nums):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i]+dfs(i+2),dfs(i+1)) # Rob this house and next house nums[i]+dfs(i+2)
                                                # or from next houses dfs(i+1)

            return memo[i]
        return dfs(0)
