class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ans = len(nums)
        for i, n in enumerate(nums):
            ans ^= i
            ans ^= n
        return ans
        