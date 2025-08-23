class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_length = 0

        def find_max_length(ind, cur_lst):
            if ind == len(nums)-1:
                return 1
            
            
            max_length = max(max_length,len(cur_lst))


        res = max([find_max_length(i,[]) for i in nums])
        return res