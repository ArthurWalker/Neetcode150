class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i+ nums[i] >=goal:
                goal = i
        
        return True if goal == 0 else False

# The idea is to go backward and we start from the last position. Because the goal is to reach there
# To reach there, the previous position need to reach there, so our new goal is len(nums)-2
# To reach there, the previous position need to reach there, so our new goal is len(nums)-3
# To reach there, we will do the same until the goal position is now 0. If it is then it means, it can reach the last destination