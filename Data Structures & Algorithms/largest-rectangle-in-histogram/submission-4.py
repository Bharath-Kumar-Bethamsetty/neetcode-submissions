class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [-1]
        n = len(heights)
        best = 0

        for i, h in enumerate(heights + [0]):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)
        
        return best

