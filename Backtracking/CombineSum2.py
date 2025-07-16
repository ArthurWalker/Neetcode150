class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = [] 

        def dfs(i,curr):
            total = sum(curr.copy())

            if total == target:
                if curr.copy() not in res:
                    res.append(curr.copy())
                return

            if i >= len(candidates) or  total > target:
                return

            candidate = candidates[i]
            
            # Left node
            curr.append(candidate)
            dfs(i+1,curr)

            # Right node
            curr.pop()
            dfs(i+1,curr)

        dfs(0,[])
        return res

       