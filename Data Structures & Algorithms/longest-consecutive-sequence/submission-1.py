class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        nums.sort()
        ans = 1
        c = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                c += 1
            else:
                ans = max(ans, c)
                c = 1
        return max(ans, c)


