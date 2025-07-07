class Solution:
    def get_product(self,s,inde):
        res = 1
        for i in range(len(s)):
            if i!=inde:
                res*=s[i]
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        for i,v in enumerate(nums):
            temp = self.get_product(nums,i)
            res.append(temp) 
        return res  