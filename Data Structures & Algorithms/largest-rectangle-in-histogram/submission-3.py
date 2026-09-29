class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                nse = i
                pse = -1 if not stack else stack[-1]
                area = h * (nse - pse - 1)
                maxArea = max(maxArea, area)
            stack.append(i)
        
        while stack:
            nse = n
            h = heights[stack.pop()]
            pse = -1 if not stack else stack[-1]
            area = h * (nse - pse - 1)
            maxArea = max(maxArea, area)
        
        return maxArea

