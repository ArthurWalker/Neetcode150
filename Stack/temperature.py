
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(temp)
            else:
                count = 0
                while len(stack) > 0 and temp > stack[-1]:
                    count+=1
                    if output[day-count]==0:
                        stack.pop()
                        output[day-count] = count 
                if len(stack)==0 or temp <= stack[-1]:
                    stack.append(temp)
        return output