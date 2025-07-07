class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dicta = {}
        for i in set(nums):
            if nums.count(i) > 1:
                return i