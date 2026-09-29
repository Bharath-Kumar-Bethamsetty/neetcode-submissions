class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights)-1
        m = -float('inf')

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            m = max(m, height*width)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return m

        