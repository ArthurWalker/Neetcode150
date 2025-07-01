class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_val = len(set(nums))
        if len_val == len(nums):
            return False
        else:
            return True