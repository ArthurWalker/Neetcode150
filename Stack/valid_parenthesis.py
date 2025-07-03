class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) ==1:
            return False
        stack = []
        dicta = {'(':')','{':'}','[':']'}
        for i,n in enumerate(s):
            if n in dicta:
                stack.append(n)
            elif len(stack) > 0 and dicta[stack[-1]]==n:
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        return False
