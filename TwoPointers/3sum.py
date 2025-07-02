class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,cur in enumerate(nums):
            target = cur
            if i>0 and cur == nums[i-1]: # skip duplicated values
                continue
            left,right = i+1, len(nums)-1
            while left < right:
                sum_3 = target+ nums[left]+nums[right]
                if sum_3 < 0:
                    left+=1
                elif sum_3 > 0:
                    right-=1
                else:
                    res.append([nums[left],nums[right],target])
                    left+=1
                    while nums[left]== nums[left-1] and left < right:
                        left +=1
        return res