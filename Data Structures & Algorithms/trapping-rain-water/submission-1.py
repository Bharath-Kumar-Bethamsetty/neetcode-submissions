class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_max = []
        right_max = [0] * (n)

        curr_left_max = height[0]
        curr_right_max = height[-1]

        for h in height:
            curr_left_max = max(curr_left_max, h)
            left_max.append(curr_left_max)
        
        for i in range(n-1, -1, -1):
            curr_right_max = max(curr_right_max, height[i])
            right_max[i] = curr_right_max
        
        total = 0
        for i in range(n):
            total += min(left_max[i], right_max[i]) - height[i]

        return total