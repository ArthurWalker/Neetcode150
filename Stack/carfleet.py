class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []  # contain time to destination
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    


    # The idea is that first we need to sort by position and reverse so that the stack
    # can go from left to right

    # The main idea is that as long as the time of next car to the destination is less than the time of previous car
    # then it will meet at some point and it will become one or fleet. So as long as the time of next to the next
    # destination is higher then it will create a new fleet. 

    # Keep in mind that stack contain time to destination