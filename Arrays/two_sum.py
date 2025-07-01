class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta = {}
        for i,v in enumerate(nums):
            if (target - v) not in dicta:
                dicta[v] = i
            else:
                if v == target-v:
                    return [dicta[v],i]
                else:
                    dicta[v] = i
                    return [dicta[target-v],dicta[v]]
        return