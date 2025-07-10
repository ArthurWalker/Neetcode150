class Solution:

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
        
    #     for num in nums:
    #         res += [subset + [num] for subset in res]
        
    #     return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort() # sort the numbers to handle duplicates

        def backtrack(start,current):
            # add current subset to the final result
            result.append(list(current))

            # iterate over nums to generate all possible subsets
            for i in range(start,len(nums)):
                # skip the duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                current.append(nums[i]) #1. include nums[i] in the current subset
                backtrack(i+1,current) #2.  and move forward
                current.pop() #3. exclude nums[i] from current subset(backtrack)
        
            return nums
    
        backtrack(0,[])  # interate backtracking
        return result