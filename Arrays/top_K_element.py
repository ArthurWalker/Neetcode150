class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        arr = []
        for ele in set_nums:
            arr.append([ele,nums.count(ele)])
        new_arr = sorted(arr,key =lambda x:x[1])[::-1]
        return [i[0] for i in new_arr[:k]]
