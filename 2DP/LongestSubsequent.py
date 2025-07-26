class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def dfs(po1,po2):
            if po1 == len(text1) or po2 == len(text2):
                return 0
            print(po1,po2)
            if (po1,po2) in memo:
                return memo[(po1,po2)]
           
            if text1[po1] == text2[po2]:
                memo[(po1,po2)]  =  1 + dfs(po1+1,po2+1)
            else:
                memo[(po1,po2)]= max(dfs(po1+1,po2),dfs(po1,po2+1))
            return memo[(po1,po2)]
        
        return dfs(0,0)