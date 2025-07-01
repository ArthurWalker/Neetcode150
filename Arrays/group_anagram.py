class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicta = {}
        for substr in strs:
            new_s = ''.join(sorted(substr))
            if new_s not in dicta:
                dicta[new_s] = [substr]
            else:
                dicta[new_s].append(substr)
        return [v for k, v in dicta.items()]
