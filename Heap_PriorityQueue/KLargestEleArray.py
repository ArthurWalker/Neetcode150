class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        new_nums = [-num for num in nums]
        heapq.heapify(new_nums)
        while k > 0:
            temp_res = -1*heapq.heappop(new_nums)
            print(temp_res)
            k-=1
        
        return temp_res

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[len(nums) - k]