class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        stack = []
        def backtrack(openPara,closePara):
            if openPara == closePara == n:
                res.append("".join(stack))
                return
           
            if openPara < n:
                stack.append('(')
                backtrack(openPara+1,closePara)
                stack.pop()
            if closePara < openPara:
                stack.append(')')
                backtrack(openPara,closePara+1)
                stack.pop()
        backtrack(0,0)
        return res