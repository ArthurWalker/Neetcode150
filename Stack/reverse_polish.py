class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1 and tokens[0] not in "+-*/":
            return int(tokens[0])
        stack = []
        for char in tokens:
            if char not in "+-*/":
                stack.append(char)
            else:
                right_n = int(stack.pop())
                left_n = int(stack.pop())
                if char == '+':
                    res = right_n+left_n
                elif char == '-':
                    res = left_n-right_n
                elif char == '*':
                    res = right_n*left_n
                else:
                    res = left_n/right_n
                stack.append(res)
        return int(stack[0]) 