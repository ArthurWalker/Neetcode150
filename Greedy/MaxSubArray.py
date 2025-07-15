class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        maxi =  float('-inf')
        res = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                print(nums[i:j])
                if maxi < sum(nums[i:j+1]):
                    maxi = sum(nums[i:j+1])
                    res = nums[i:j]

        return maxi
