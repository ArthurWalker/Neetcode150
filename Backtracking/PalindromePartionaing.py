class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalpha() or i.isdigit()])
        return s==s[::-1]

    def all_Palindrome(self,lst: List[str]) -> bool:
        res = [self.isPalindrome(s) for s in lst]
        return all(res)==True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i,subset):
            
            # Base to add
            if i == len(s):
                if self.all_Palindrome(subset) and subset.copy() not in res:
                    res.append(subset.copy())
                return

            # Tach
            subset.append(s[i])
            dfs(i + 1,subset)

            # Ghep
            subset.pop()
            if len(subset)==0:
                subset = [s[i]]
            else:
                subset[-1]+=s[i]
            dfs(i + 1,subset)

        dfs(0,[])
        return res