class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        if len(heights)==2:
            max_area = min(heights[left],heights[right])
        else:
            max_area = heights[0]
        while left < right:
            area = min(heights[left],heights[right])*(right-left)
            if area >= max_area:
                print(left,right,heights[left],heights[right])
                max_area = area
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_area